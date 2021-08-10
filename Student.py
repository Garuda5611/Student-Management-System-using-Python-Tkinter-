from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
class Student:
    try:
        def __init__(self,root):
            self.root=root
            self.root.title("Student Management System")
            self.root.geometry("1350x700+0+0")
            title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
            title.pack(side=TOP,fill=X)
            #allvariables
            self.Roll_No_var=StringVar()
            self.name_var=StringVar()
            self.email_var=StringVar()
            self.gender_var=StringVar()
            self.contact_var=StringVar()
            self.dob_var=StringVar()
            self.search_by=StringVar()
            self.search_txt=StringVar()
            #manage
            Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
            Manage_Frame.place(x=20,y=100,width=450,height=600)
            
            m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
            m_title.grid(row=0,columnspan=2,pady=20)
            
            lbl_roll=Label(Manage_Frame,text="Roll No",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
            txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),textvariable=self.Roll_No_var,bd=5,relief=GROOVE)
            txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
            txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),textvariable=self.name_var,bd=5,relief=GROOVE)
            txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
            txt_Email=Entry(Manage_Frame,font=("times new roman",15,"bold"),textvariable=self.email_var,bd=5,relief=GROOVE)
            txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

            lbl_gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
            combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",13,"bold"),textvariable=self.gender_var,state="readonly")
            combo_gender['values']=('Male','Female','Other')
            combo_gender.grid(row=4,column=1,pady=10,padx=20)
            
            lbl_contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
            txt_Contact=Entry(Manage_Frame,font=("times new roman",15,"bold"),textvariable=self.contact_var,bd=5,relief=GROOVE)
            txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")
            
            lbl_dob=Label(Manage_Frame,text="D. O. B.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
            txt_Dob=Entry(Manage_Frame,font=("times new roman",15,"bold"),textvariable=self.dob_var,bd=5,relief=GROOVE)
            txt_Dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

            lbl_add=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_add.grid(row=7,column=0,pady=10,padx=20,sticky="w")
            self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("times new roman",10,"bold"))
            self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

            #Button
            btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
            btn_Frame.place(x=15,y=530,width=420)

            addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
            updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
            deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
            clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

            #detail
            Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
            Detail_Frame.place(x=500,y=100,width=800,height=600)

            lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
            combo_search=ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by,font=("times new roman",13,"bold"),state="readonly")
            combo_search['values']=('Roll_no','Name','Contact')
            combo_search.grid(row=0,column=1,pady=10,padx=20)

            txt_search=Entry(Detail_Frame,width=20,textvariable=self.search_txt,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
            txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
            searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
            showbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

            #table_frame
            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=10,y=70,width=760,height=500)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
            self.Student_table=ttk.Treeview(Table_Frame,columns=("roll_no","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Student_table.xview)
            scroll_y.config(command=self.Student_table.yview)
            self.Student_table.heading("roll_no",text="Roll No.")
            self.Student_table.heading("name",text="Name")
            self.Student_table.heading("email",text="Email")
            self.Student_table.heading("gender",text="Gender")
            self.Student_table.heading("contact",text="Contact")
            self.Student_table.heading("dob",text="DOB")
            self.Student_table.heading("Address",text="Address")
            self.Student_table['show']='headings'
            self.Student_table.column("roll_no",width=80)
            self.Student_table.column("name",width=110)
            self.Student_table.column("email",width=110)
            self.Student_table.column("gender",width=110)
            self.Student_table.column("contact",width=110)
            self.Student_table.column("dob",width=110)
            self.Student_table.column("Address",width=130)
            self.Student_table.pack(fill=BOTH,expand=1)
            self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()
        def add_student(self):
            if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
                messagebox.showerror("Error","All Fields are Required!!")
            else:
                con=pymysql.connect(host="localhost",user="root",port=3306,password="root",database="stm",cursorclass=pymysql.cursors.DictCursor)
                try:
                    with con.cursor() as cursor:
                        sqlq="INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sqlq,(self.Roll_No_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END)))
                        con.commit()
                        self.fetch_data()
                        self.clear()
                finally:
                    con.close()
                messagebox.showinfo("Success","Record has been inserted")
        def fetch_data(self):
            con=pymysql.connect(host="localhost",user="root",password="root",database="stm")
            cursor=con.cursor()
            cursor.execute("select * from student")
            rows=cursor.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            con.close()
        def clear(self):
            self.Roll_No_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_Address.delete("1.0",END)
        def get_cursor(self,ev):
            cursor_row=self.Student_table.focus()
            content=self.Student_table.item(cursor_row)
            row=content['values']
            self.Roll_No_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.dob_var.set(row[5])
            self.txt_Address.delete("1.0",END)
            self.txt_Address.insert(END,row[6])
        def update_data(self):
            if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
                messagebox.showerror("Error","All Fields are Required!!")
            else:
                con=pymysql.connect(host="localhost",user="root",password="root",database="stm")
                cursor=con.cursor()
                cursor.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),
                                                                                                                              self.email_var.get(),
                                                                                                                              self.gender_var.get(),
                                                                                                                              self.contact_var.get(),
                                                                                                                              self.dob_var.get(),
                                                                                                                              self.txt_Address.get('1.0',END),
                                                                                                                              self.Roll_No_var.get()
                                                                                                                              ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been updated")
        def delete_data(self):
            if self.Roll_No_var.get()=="":
                messagebox.showerror("Error","Roll No is required!!")
            else:
                con=pymysql.connect(host="localhost",user="root",password="root",database="stm")
                cursor=con.cursor()
                cursor.execute("delete from student where roll_no=%s",self.Roll_No_var.get())
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success","Record has been deleted")
        def search_data(self):
            if self.search_txt.get()=="" or self.search_by.get()=="":
                messagebox.showerror("Error","Search Fields are Required!!")
            else:
                con=pymysql.connect(host="localhost",user="root",password="root",database="stm")
                cursor=con.cursor()
                cursor.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows=cursor.fetchall()
                if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                        self.Student_table.insert('',END,values=row)
                    con.commit()
                con.close()
    except IntegrityError:
         messagebox.showerror("Error","Student with same roll number already exists!!")
         self.Roll_No_var.set("")
         self.name_var.set("")
         self.email_var.set("")
         self.gender_var.set("")
         self.contact_var.set("")
         self.dob_var.set("")
         self.txt_Address.delete("1.0",END)
root=Tk()
ob=Student(root)
root.mainloop()
