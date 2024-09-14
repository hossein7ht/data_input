from tkinter import *
from tkinter import messagebox
import sqlite3

#function________________________________
def check_star():
    if ent_fname.get()=="":
        lbl_fname.configure(text="*fname:",fg="#e00000")
    else:
        lbl_fname.configure(text=" fname:",fg="#000000")
    
    if ent_lname.get()=="":
        lbl_lname.configure(text="*lname:",fg="#e00000")
    else:
        lbl_lname.configure(text=" lname:",fg="#000000")
    
    if ent_city.get()=="":
        lbl_city.configure(text="*city:",fg="#e00000")
    else:
        lbl_city.configure(text=" city:",fg="#000000")
    
    if ent_phone.get()=="":
        lbl_phone.configure(text="*phone:",fg="#e00000")
    else:
        lbl_phone.configure(text=" phone:",fg="#000000")
    
    win.after(50,check_star)

def show_rbn(bind):
    rbn_fname.place(x=4,y=38)
    rbn_lname.place(x=344,y=38)
    rbn_city.place(x=4,y=118)
    rbn_phone.place(x=344,y=118)
    
def hide_rbn(bind):
    rbn_fname.place_forget()
    rbn_lname.place_forget()
    rbn_city.place_forget()
    rbn_phone.place_forget()

def reload(bind):
    if ent_serch.get()=="":
        lst_data.delete(0,END)
        cur.execute("select * from person order by lname,fname,city")
        records=cur.fetchall()
        c=0
        for record in records:
            c+=1
            j_record=" ".join(record)
            lst_data.insert(END,f"{c}-{j_record}")

def fetch(bind):
    try:
        global d
        index=lst_data.curselection()
        data=lst_data.get(index)
        f=data.split("-")
        d=f[1].split( )
        ent_fname.delete(0,"end")
        ent_lname.delete(0,"end")
        ent_city.delete(0,"end")
        ent_phone.delete(0,"end")
        ent_fname.insert(0,d[0])
        ent_lname.insert(0,d[1])
        ent_city.insert(0,d[2])
        ent_phone.insert(0,d[3])
    except:
        pass

def serch():
    if ent_serch.get()=="":
        pass
        
    else:    
        lst_data.delete(0,END)
        if selected_option.get()=="Option1":
            name=ent_serch.get().lower()
            fname=""
            for i in name:
                if i=='*':
                    fname+='%'
                elif i=='?':
                    fname+='_'
                else:
                    fname+=i
            cur.execute("select * from person where fname like? order by lname,fname,city",(fname,))
            records=cur.fetchall()
            c=0
            for record in records:
                c+=1
                j_record=" ".join(record)
                lst_data.insert(END,f"{c}-{j_record}")
        
        elif selected_option.get()=="Option2":
            family=ent_serch.get().lower()
            lname=""
            for i in family:
                if i=='*':
                    lname+='%'
                elif i=='?':
                    lname+='_'
                else:
                    lname+=i
            cur.execute("select * from person where lname like? order by lname,fname,city",(lname,))
            records=cur.fetchall()
            c=0
            for record in records:
                c+=1
                j_record=" ".join(record)
                lst_data.insert(END,f"{c}-{j_record}")

        elif selected_option.get()=="Option3":
            shahr=ent_serch.get().lower()
            city=""
            for i in shahr:
                if i =='*':
                    city+='%'
                elif i=='?':
                    city+='_'
                else:
                    city+=i
            cur.execute("select * from person where city like? order by lname,fname,city",(city,))
            records=cur.fetchall()
            c=0
            for record in records:
                c+=1
                j_record=" ".join(record)
                lst_data.insert(END,f"{c}-{j_record}")

        else:
            tel=ent_serch.get().lower()
            phone=""
            for i in tel:
                if i =='*':
                    phone+='%'
                elif i=='?':
                    phone+='_'
                else:
                    phone+=i
            cur.execute("select * from person where phone like? order by lname,fname,city",(phone,))
            records=cur.fetchall()
            c=0
            for record in records:
                c+=1
                j_record=" ".join(record)
                lst_data.insert(END,f"{c}-{j_record}")

def insert():
    if ent_fname.get()=="" or ent_lname.get()=="" or ent_city.get()=="" or ent_phone.get()=="":
        pass
    
    elif ent_fname.get().isalpha()==False:
        messagebox.showerror("Error","The entered fname is invalid")

    elif ent_lname.get().isalpha()==False:
        messagebox.showerror("Error","The entered lname is invalid")

    elif ent_city.get().isalpha()==False:
        messagebox.showerror("Error","The entered city is invalid")
    
    elif ent_phone.get().isdigit()==False:
        messagebox.showerror("Error","The entered phone number is invalid")
    else:
        try:
            fname=ent_fname.get().lower()
            lname=ent_lname.get().lower()
            city=ent_city.get().lower()
            phone=ent_phone.get()
            cur.execute("insert into person(fname,lname,city,phone) values(?,?,?,?)",(fname,lname,city,phone))
            con.commit()
            print("record inserted")
            lst_data.insert("end",f"{fname} {lname} {city} {phone}")
            ent_fname.delete(0,"end")
            ent_lname.delete(0,"end")
            ent_city.delete(0,"end")
            ent_phone.delete(0,"end")
            ent_fname.focus_set()
            lst_data.delete(0,END)
            cur.execute("select * from person order by lname,fname,city")
            records=cur.fetchall()
            c=0
            for record in records:
                c+=1
                j_record=" ".join(record)
                lst_data.insert(END,f"{c}-{j_record}")
        except:
            messagebox.showerror("Error","You entered a duplicate phone number")

def update():
    if ent_fname.get()=="" or ent_lname.get()=="" or ent_city.get()=="" or ent_phone.get()=="":
       pass
    
    elif ent_fname.get().isalpha()==False:
        messagebox.showerror("Error","The enterded fname is invalid")

    elif ent_lname.get().isalpha()==False:
        messagebox.showerror("Error","The entered lname is invalid")

    elif ent_city.get().isalpha()==False:
        messagebox.showerror("Error","The entered city is invalid")
    
    elif ent_phone.get().isdigit()==False:
        messagebox.showerror("Error","The entered phone number is invalid")
    else:
        try:
            fname=ent_fname.get().lower()
            lname=ent_lname.get().lower()
            city=ent_city.get().lower()
            phone=ent_phone.get()
            cur.execute("update person set fname=?,lname=?,city=?,phone=? where phone=?",(fname,lname,city,phone,d[3]))
            con.commit()
            print("record updated")
            ent_fname.delete(0,"end")
            ent_lname.delete(0,"end")
            ent_city.delete(0,"end")
            ent_phone.delete(0,"end")
            ent_fname.focus_set()
            lst_data.delete(0,END)
            cur.execute("select * from person order by lname,fname,city")
            records=cur.fetchall()
            c=0
            for record in records:
                c+=1
                j_record=" ".join(record)
                lst_data.insert(END,f"{c}-{j_record}")
        except NameError:
            pass
        
        except sqlite3.IntegrityError:
            messagebox.showerror("Error","You entered a duplicate phone number")

def delete():
    index=lst_data.curselection()
    if len(index)!=0:
        data=lst_data.get(index)
        d=data.split()
        cur.execute("delete from person where phone=?",(d[3],)) 
        con.commit()  
        print("record deleted")
        lst_data.delete(0,END)
        ent_fname.delete(0,"end")
        ent_lname.delete(0,"end")
        ent_city.delete(0,"end")
        ent_phone.delete(0,"end")
        ent_fname.focus_set()
        cur.execute("select * from person order by lname,fname,city")
        records=cur.fetchall()
        c=0
        for record in records:
            c+=1
            j_record=" ".join(record)
            lst_data.insert(END,f"{c}-{j_record}")

def exit():
    resault=messagebox.askyesno("Warning","Are you sure to exit?")
    if resault==TRUE:
        con.close()
        win.destroy()

#mainsetting_____________________________
win=Tk()
win.title("data_input")
w0=win.winfo_screenwidth()//2
h0=win.winfo_screenheight()//2
width=700
height=500
w=w0-width//2
h=h0-height//2
win.geometry(f"{width}x{height}+{w}+{h}")
win.resizable(0,0)
win.configure(bg="#e7f1ff")
con=sqlite3.connect("d:/data_input.db")
cur=con.cursor()
cur.execute("create table if not exists person(fname text,lname text,city text,phone text primary key)")
con.commit()
    
#widget_____________________________Label
lbl_fname=Label(win,text="*fname:",font="arial 20 bold",bg="#e7f1ff",fg="#000000")
lbl_fname.place(x=20,y=20)

lbl_lname=Label(win,text="*lname:",font="arial 20 bold",bg="#e7f1ff",fg="#000000")
lbl_lname.place(x=360,y=20)

lbl_city=Label(win,text="*city:",font="arial 20 bold",bg="#e7f1ff",fg="#000000")
lbl_city.place(x=20,y=100)

lbl_phone=Label(win,text="*phone:",font="arial 20 bold",bg="#e7f1ff",fg="#000000")
lbl_phone.place(x=360,y=100)

#widget_____________________________Entry
ent_fname=Entry(win,font="arial 20",width=12)
ent_fname.place(x=140,y=20)

ent_lname=Entry(win,font="arial 20",width=12)
ent_lname.place(x=480,y=20)

ent_city=Entry(win,font="arial 20",width=12)
ent_city.place(x=140,y=100)

ent_phone=Entry(win,font="arial 20",width=12)
ent_phone.place(x=480,y=100)

ent_serch=Entry(win,font="arial 15",width=41)
ent_serch.place(x=59,y=170)

#widget_______________________Radiobutton
selected_option=StringVar(value="Option2")

rbn_fname=Radiobutton(win,bg="#e7f1ff",variable=selected_option,value="Option1")
rbn_fname.place_forget()

rbn_lname=Radiobutton(win,bg="#e7f1ff",variable=selected_option,value="Option2")
rbn_lname.place_forget()

rbn_city=Radiobutton(win,bg="#e7f1ff",variable=selected_option,value="Option3")
rbn_city.place_forget()

rbn_phone=Radiobutton(win,bg="#e7f1ff",variable=selected_option,value="Option4")
rbn_phone.place_forget()

#widget____________________________Button
btn_serch=Button(win,text="serch",font="arial 10",width=14,bg="#007bff",fg="#ffffff",command=serch)
btn_serch.place(x=520,y=170)

btn_insert=Button(win,text="insert",font="arial 20",width=7,bg="#007bff",fg="#ffffff",command=insert)
btn_insert.place(x=59,y=420)

btn_update=Button(win,text="update",font="arial 20",width=7,bg="#007bff",fg="#ffffff",command=update)
btn_update.place(x=210,y=420)

btn_delete=Button(win,text="delete",font="arial 20",width=7,bg="#007bff",fg="#ffffff",command=delete)
btn_delete.place(x=365,y=420)

btn_exit=Button(win,text="exit",font="arial 20",width=7,bg="#B70922",fg="#ffffff",command=exit)
btn_exit.place(x=520,y=420)

#widget_________________________Scrollbar
scr_data=Scrollbar(win)
scr_data.place(x=624,y=200,height=205)

#widget___________________________Listbox
lst_data=Listbox(win,font="arial 19",width=40,yscrollcommand=scr_data.set,bd=2)
lst_data.place(x=58,y=200,height=205)
scr_data.configure(command=lst_data.yview)



cur.execute("select * from person order by lname,fname,city")
records=cur.fetchall()
c=0
for record in records:
    c+=1
    j_record=" ".join(record)
    lst_data.insert(END,f"{c}-{j_record}")
check_star()
win.bind("<<ListboxSelect>>",fetch)
win.bind("<Control_L>",show_rbn)
win.bind("<KeyRelease-Control_L>",hide_rbn)
win.bind("<KeyRelease>",reload)
win.mainloop()