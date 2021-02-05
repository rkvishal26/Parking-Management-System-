import tkinter as tk
from tkinter import ttk
from tkinter import font  as tkfont 
from tkinter import messagebox
import sqlite3

with sqlite3.connect("parking.db") as db:
    cursur = db.cursor()
    cursur.execute("CREATE TABLE IF NOT EXISTS User(ID TEXT NOT NULL PRIMARY KEY,Password TEXT,first_name TEXT,last_name TEXT,phone_number TEXT,email TEXT,designation TEXT,Department TEXT,block TEXT,wheel TEXT,color TEXT,adhar TEXT,licence TEXT,rc TEXT,pay_details TEXT);")
    cursur.execute("CREATE TABLE IF NOT EXISTS Log(block TEXT,vehicle_no TEXT,vehicle_color TEXT,vehicle_type TEXT,email TEXT,entry_time TEXT,licence TEXT,rc TEXT,phn TEXT);")
    cursur.execute("SELECT * FROM User")
    db.commit()
db.close()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Arial', size=22, weight="bold")
        self.title("Parking Management System")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Application, Login, Register, Admin_login, Temporary_Parking, Feedback, Register_Admin, Admin, Powers):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="wens")

        self.show_frame("Application")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
class Application(tk.Frame):
    #initialize tk() inherited class
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    #create canvas
    def create_widgets(self):
        self.canvas = tk.Canvas(self , width = 800 , height = 600 , bd = 0 , highlightthickness = 2)
        self.canvas.grid(row=0,column=0)

        self.img1= tk.PhotoImage(file="C:\\Users\\anish\\Downloads\\User_login.png")
        self.img2= tk.PhotoImage(file="C:\\Users\\anish\\Downloads\\adminlogin_s.png")
        self.img3= tk.PhotoImage(file="C:\\Users\\anish\\Downloads\\housing_visitor-registration.png")
        self.img4= tk.PhotoImage(file="C:\\Users\\anish\\Downloads\\parking.png")
        self.img5= tk.PhotoImage(file="C:\\Users\\anish\\Downloads\\feedback.png")

        self.login_button = tk.Button(self.canvas , text="not found" , image = self.img1 , command = lambda: self.controller.show_frame("Login"))
        self.login_button.grid(column = 0 , row = 0)
        
        self.admin_login = tk.Button(self.canvas , text="not found" , image = self.img2 , command = lambda: self.controller.show_frame("Admin_login"))
        self.admin_login.grid(column = 1 , row = 0)
        
        self.register = tk.Button(self.canvas , text="not found" , image = self.img3 , command = lambda: self.controller.show_frame("Register"))
        self.register.grid(column = 2 , row = 0)
        
        self.temp_park = tk.Button(self.canvas , text="not found" , image = self.img4 , command = lambda: self.controller.show_frame("Temporary_Parking"))
        self.temp_park.grid(column = 3 , row = 0)
        
        self.feed_back = tk.Button(self.canvas , text="not found" , image = self.img5 , command = lambda: self.controller.show_frame("Feedback"))
        self.feed_back.grid(column = 4, row = 0)
        
        self.login_text = tk.Label(self.canvas , text="Login")
        self.login_text.grid(column = 0 , row = 1)
        
        self.login_text = tk.Label(self.canvas , text="Admin Login")
        self.login_text.grid(column = 1 , row = 1)
        
        self.register_text = tk.Label(self.canvas , text="Register")
        self.register_text.grid(column = 2 , row = 1)
        
        self.temp_park_text = tk.Label(self.canvas , text="Temp-Parking")
        self.temp_park_text.grid(column = 3 , row = 1)
        
        self.temp_park_text = tk.Label(self.canvas , text="Feedback")
        self.temp_park_text.grid(column = 4 , row = 1)
        
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.login()
        
    def login_submit(self):
        with sqlite3.connect("parking.db") as db:
            cursur = db.cursor()
        find_user = ("SELECT * FROM user WHERE ID = ? AND Password = ?")
        cursur.execute(find_user,[(self.user_name_field.get()),(self.password_field.get())])
        results = cursur.fetchall()
        if results:
            self.controller.show_frame("Temporary_Parking")
        else:
            messagebox.showerror("Oops!!","Wrong username or password")

    
            
    def login(self):
        self.lcanvas_data = tk.Canvas(self , width = 500 , height = 600 , bd = 0 , highlightthickness = 2)
        self.lcanvas_data.grid(row=0,column=0)

        self.user_name = tk.Label(self.lcanvas_data , text = "RF ID")
        self.user_name.grid(row = 0,column = 0)

        self.user_name_field = tk.Entry(self.lcanvas_data , textvariable = self.username)
        self.user_name_field.grid(row = 0 , column = 1)

        self.password = tk.Label(self.lcanvas_data , text = "Password")
        self.password.grid(row = 1,column = 0)

        self.password_field = tk.Entry(self.lcanvas_data , show = "*" , textvariable = self.password)
        self.password_field.grid(row = 1 , column = 1)

        self.login_button = tk.Button(self.lcanvas_data , text = "Login" , command = self.login_submit)
        self.login_button.grid(row = 2 , column = 1)

        self.register = tk.Button(self.lcanvas_data , text="Register" , command = lambda: self.controller.show_frame("Register"))
        self.register.grid(column = 2 , row = 2)

        self.Index = tk.Button(self.lcanvas_data , text="Back" , command = lambda: self.controller.show_frame("Application"))
        self.Index.grid(column = 0 , row = 2)
        
class Admin_login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.login()
        
    def login_submit(self):
        with sqlite3.connect("parking.db") as db:
            cursur = db.cursor()
        find_user = ("SELECT * FROM user WHERE ID = ? AND Password = ?")
        cursur.execute(find_user,[(self.user_name_field.get()),(self.password_field.get())])
        results = cursur.fetchall()
        if results:
            self.controller.show_frame("Admin")
        else:
            messagebox.showerror("Oops!!","Wrong username or password")

    
            
    def login(self):
        self.lcanvas_data = tk.Canvas(self , width = 500 , height = 600 , bd = 0 , highlightthickness = 2)
        self.lcanvas_data.grid(row=0,column=0)

        self.user_name = tk.Label(self.lcanvas_data , text = "Admin ID")
        self.user_name.grid(row = 0,column = 0)

        self.user_name_field = tk.Entry(self.lcanvas_data , textvariable = self.username)
        self.user_name_field.grid(row = 0 , column = 1)

        self.password = tk.Label(self.lcanvas_data , text = "Password")
        self.password.grid(row = 1,column = 0)

        self.password_field = tk.Entry(self.lcanvas_data , show = "*" , textvariable = self.password)
        self.password_field.grid(row = 1 , column = 1)

        self.login_button = tk.Button(self.lcanvas_data , text = "Login" , command = self.login_submit)
        self.login_button.grid(row = 2 , column = 1)

        self.register = tk.Button(self.lcanvas_data , text="Register" , command = lambda: self.controller.show_frame("Register_Admin"))
        self.register.grid(column = 2 , row = 2)

        self.Index = tk.Button(self.lcanvas_data , text="Back" , command = lambda: self.controller.show_frame("Application"))
        self.Index.grid(column = 0 , row = 2)

        self.Index = tk.Button(self.lcanvas_data , text="Back" , command = lambda: self.controller.show_frame("Application"))
        self.Index.grid(column = 0 , row = 2)
        
class Admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widget()

    def display_db(self):
        with sqlite3.connect("parking.db") as db:
            cursur = db.cursor()
            cursur.execute("SELECT * FROM User WHERE ID!='ADMIN' order by ID")
            result = cursur.fetchall()

        tk.Label(self.table_canvas , text = "RF.ID", borderwidth=2, relief="solid").grid(row=0 , column=0, sticky = "we")
        tk.Label(self.table_canvas , text = "First Name", borderwidth=2, relief="solid").grid(row=0 , column=1, sticky = "we")
        tk.Label(self.table_canvas , text = "Last Name", borderwidth=2, relief="solid").grid(row=0 , column=2, sticky = "we")
        tk.Label(self.table_canvas , text = "Phone No.", borderwidth=2, relief="solid").grid(row=0 , column=3, sticky = "we")
        tk.Label(self.table_canvas , text = "Email", borderwidth=2, relief="solid").grid(row=0 , column=4, sticky = "we")
        tk.Label(self.table_canvas , text = "Designation", borderwidth=2, relief="solid").grid(row=0 , column=5, sticky = "we")
        tk.Label(self.table_canvas , text = "Department", borderwidth=2, relief="solid").grid(row=0 , column=6, sticky = "we")
        tk.Label(self.table_canvas , text = "Block", borderwidth=2, relief="solid").grid(row=0 , column=7, sticky = "we")
        tk.Label(self.table_canvas , text = "Wheeler", borderwidth=2, relief="solid").grid(row=0 , column=8, sticky = "we")
        tk.Label(self.table_canvas , text = "Color", borderwidth=2, relief="solid").grid(row=0 , column=9, sticky = "we")
        tk.Label(self.table_canvas , text = "Adhar", borderwidth=2, relief="solid").grid(row=0 , column=10, sticky = "we")
        tk.Label(self.table_canvas , text = "Licence", borderwidth=2, relief="solid").grid(row=0 , column=11, sticky = "we")
        tk.Label(self.table_canvas , text = "Registeration certificate", borderwidth=2, relief="solid").grid(row=0 , column=12, sticky = "we")
        tk.Label(self.table_canvas , text = "Fee", borderwidth=2, relief="solid").grid(row=0 , column=13, sticky = "we")

        
        count = 1
        
        for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o in result:
            tk.Label(self.table_canvas , text = a, borderwidth=2, relief="solid").grid(row=count , column=0, sticky = "we")
            tk.Label(self.table_canvas , text = c, borderwidth=2, relief="solid").grid(row=count , column=1, sticky = "we")
            tk.Label(self.table_canvas , text = d, borderwidth=2, relief="solid").grid(row=count , column=2, sticky = "we")
            tk.Label(self.table_canvas , text = e, borderwidth=2, relief="solid").grid(row=count , column=3, sticky = "we")
            tk.Label(self.table_canvas , text = f, borderwidth=2, relief="solid").grid(row=count , column=4, sticky = "we")
            tk.Label(self.table_canvas , text = g, borderwidth=2, relief="solid").grid(row=count , column=5, sticky = "we")
            tk.Label(self.table_canvas , text = h, borderwidth=2, relief="solid").grid(row=count , column=6, sticky = "we")
            tk.Label(self.table_canvas , text = i, borderwidth=2, relief="solid").grid(row=count , column=7, sticky = "we")
            tk.Label(self.table_canvas , text = j, borderwidth=2, relief="solid").grid(row=count , column=8, sticky = "we")
            tk.Label(self.table_canvas , text = k, borderwidth=2, relief="solid").grid(row=count , column=9, sticky = "we")
            tk.Label(self.table_canvas , text = l, borderwidth=2, relief="solid").grid(row=count , column=10, sticky = "we")
            tk.Label(self.table_canvas , text = m, borderwidth=2, relief="solid").grid(row=count , column=11, sticky = "we")
            tk.Label(self.table_canvas , text = n, borderwidth=2, relief="solid").grid(row=count , column=12, sticky = "we")
            tk.Label(self.table_canvas , text = o, borderwidth=2, relief="solid").grid(row=count , column=13, sticky = "we")
            count = count+1


    
    def widget(self):
        self.admin_canvas = tk.Canvas(self , width = 1200 , height = 800 , highlightthickness = 2 , bd = 0)
        self.admin_canvas.pack()

        self.table_canvas = tk.Canvas(self.admin_canvas , width = 300 , height = 300 , bg = "white" , bd = 10)
        self.table_canvas.grid(row = 1 , column = 0 , columnspan = 7)

        self.display_button = tk.Button(self.admin_canvas , text = "Display", command = lambda: self.display_db())
        self.display_button.grid(row = 3 , column = 1)

            
        self.update_button = tk.Button(self.admin_canvas , text = "Change", command = lambda: self.controller.show_frame("Powers"))
        self.update_button.grid(row = 3 , column = 2)

        self.Index = tk.Button(self.admin_canvas , text="Back" , command = lambda: self.controller.show_frame("Application"))
        self.Index.grid(column = 0 , row = 3)

    
class Powers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.ID_mod= tk.StringVar()
        self.User_id_v= tk.StringVar()
        self.First_name_v= tk.StringVar()
        self.Last_name_v= tk.StringVar()
        self.Pass_word_v= tk.StringVar()
        self.V_colour_v= tk.StringVar()
        self.V_type_v= tk.StringVar()
        self.L_no_v= tk.StringVar()
        self.RC_no_v= tk.StringVar()
        self.Dept_name_v= tk.StringVar()
        self.Desig_name_v= tk.StringVar()
        self.Block_no_v= tk.StringVar()
        self.Ph_no_v= tk.StringVar()
        self.Email_id_v= tk.StringVar()
        self.Amt_pay_v= tk.StringVar()
        self.Aadhar_no_v= tk.StringVar()
        self.widget()

    def update(self):
        with sqlite3.connect("Parking.db") as db:
            cursur= db.cursor()
            update_user = ("Update User SET Password =?, first_name =?, last_name =?, phone_number =?, email =?, designation =?, Department =?, block =?, wheel =?, color =?, adhar =?, licence =?, rc =?, pay_details =? where ID = ?")
            cursur.execute(update_user,[(self.Pass_word.get()),(self.First_name.get()),(self.Last_name.get()),(self.Ph_no.get()),(self.Email_id.get()),(self.Desig_name.get()),(self.Dept_name.get()),(self.Block_no.get()),(self.V_type.get()),(self.V_colour.get()),(self.Aadhar_no.get()),(self.L_no.get()),(self.RC_no.get()),(self.Amt_pay.get()),(self.User_id.get())])
            db.commit()
        db.close()
        messagebox.showinfo("Success", "Record Succesfully UPDATED!")
        
    def delete(self):
        with sqlite3.connect("Parking.db")as db:
            cursur=db.cursor()
            delete_user=("Delete from User where ID=?")
            cursur.execute(delete_user,[(self.User_id.get())])
            db.commit()
        db.close()
        messagebox.showinfo("Success", "Record Succesfully DELETED!")
            
    def my_form(self):
        with sqlite3.connect("Parking.db") as db:
            cursur = db.cursor()
            display_user = ("SELECT * from User WHERE ID=?")
            cursur.execute(display_user,[(self.ID_mod.get())])
            result=cursur.fetchall()
            a = result[0]
            self.User_id_v.set(a[0])
            self.First_name_v.set(a[2])
            self.Last_name_v.set(a[3])
            self.Pass_word_v.set(a[1])
            self.V_colour_v.set(a[10])
            self.V_type_v.set(a[9])
            self.L_no_v.set(a[11])
            self.RC_no_v.set(a[12])
            self.Dept_name_v.set(a[7])
            self.Desig_name_v.set(a[6])
            self.Block_no_v.set(a[8])
            self.Ph_no_v.set(a[4])
            self.Email_id_v.set(a[5])
            self.Amt_pay_v.set(a[14])
            self.Aadhar_no_v.set(a[13])
                 
    def widget(self):
        self.rec_l = tk.Label(self, text="Enter the ID you want to change: ").place(x=0,y=0)
        self.rec_f = tk.Entry(self, textvariable = self.ID_mod).place(x=200,y=0)
        self.rec_b = tk.Button(self, text="Submit" , command = lambda: self.my_form()).place(x=350,y=0)


        self.Userid=tk.Label(self,text="User ID: ")
        self.User_id=tk.Entry(self,bd=5, textvariable = self.User_id_v)
        self.Userid.place(x=0,y=25)
        self.User_id.place(x=100,y=25)


        self.Firstname = tk.Label(self,text="Username: ")
        self.First_name = tk.Entry(self,bd=5, textvariable = self.First_name_v)
        self.Firstname.place(x=0,y=50)
        self.First_name.place(x=100,y=50)

        
        self.Lastname=tk.Label(self,text="Username: ")
        self.Last_name=tk.Entry(self,bd=5, textvariable = self.Last_name_v)
        self.Lastname.place(x=0,y=75)
        self.Last_name.place(x=100,y=75)

        
        self.Pass=tk.Label(self,text="Password: ")
        self.Pass_word=tk.Entry(self,bd=5, textvariable = self.Pass_word_v)
        self.Pass.place(x=0,y=100)
        self.Pass_word.place(x=100,y=100)

        
        self.Vcolour=tk.Label(self,text="Vehicle colour:  ")
        self.V_colour=tk.Entry(self,bd=5, textvariable = self.V_colour_v)
        self.Vcolour.place(x=0,y=125)
        self.V_colour.place(x=100,y=125)


        self.Vtype=tk.Label(self,text="Vehicle type: ")
        self.V_type=tk.Entry(self,bd=5, textvariable = self.V_type_v)
        self.Vtype.place(x=0,y=150)
        self.V_type.place(x=100,y=150)

        
        self.Lno=tk.Label(self,text="Licence no.: ")
        self.L_no=tk.Entry(self,bd=5, textvariable = self.L_no_v)
        self.Lno.place(x=0,y=175)
        self.L_no.place(x=100,y=175)

        
        self.RCno=tk.Label(self,text="RC no.: ")
        self.RC_no=tk.Entry(self,bd=5, textvariable = self.RC_no_v)
        self.RCno.place(x=0,y=200)
        self.RC_no.place(x=100,y=200)

        
        self.Dept=tk.Label(self,text="Department: ")
        self.Dept_name=tk.Entry(self,bd=5, textvariable = self.Dept_name_v)
        self.Dept.place(x=0,y=225)
        self.Dept_name.place(x=100,y=225)

        
        self.Desig=tk.Label(self,text="Designation: ")
        self.Desig_name=tk.Entry(self,bd=5, textvariable = self.Desig_name_v)
        self.Desig.place(x=0,y=250)
        self.Desig_name.place(x=100,y=250)

        
        self.Block=tk.Label(self,text="Block no.: ")
        self.Block_no=tk.Entry(self,bd=5, textvariable = self.Block_no_v)
        self.Block.place(x=0,y=275)
        self.Block_no.place(x=100,y=275)

        
        self.Phno=tk.Label(self,text="Phone no.: ")
        self.Ph_no=tk.Entry(self,bd=5, textvariable = self.Ph_no_v)
        self.Phno.place(x=0,y=300)
        self.Ph_no.place(x=100,y=300)


        
        self.Emailid=tk.Label(self,text="Email ID: ")
        self.Email_id=tk.Entry(self,bd=5, textvariable = self.Email_id_v)
        self.Emailid.place(x=0,y=325)
        self.Email_id.place(x=100,y=325)

        
        self.Amt=tk.Label(self,text="Amount: ")
        self.Amt_pay=tk.Entry(self,bd=5, textvariable = self.Amt_pay_v)
        self.Amt.place(x=0,y=350)
        self.Amt_pay.place(x=100,y=350)      


        
        self.Aadharno=tk.Label(self,text="Aadhar no.: ")
        self.Aadhar_no=tk.Entry(self,bd=5, textvariable = self.Aadhar_no_v)
        self.Aadharno.place(x=0,y=375)
        self.Aadhar_no.place(x=100,y=375)


        self.update=tk.Button(self,text="Update" , command = self.update)
        self.update.place(x=0,y=400)

        self.delete=tk.Button(self,text="Delete" , command = self.delete)
        self.delete.place(x=50,y=400)
        
        self.Index = tk.Button(self , text="Exit" , command = lambda: self.controller.show_frame("Application"))
        self.Index.place(x=100,y=400)
        
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.id = tk.StringVar()
        self.password = self.id.get()
        self.phone_number = tk.StringVar()
        self.email = tk.StringVar()
        self.designation = tk.StringVar()
        self.Department = tk.StringVar()
        self.block = tk.StringVar()
        self.wheel = tk.StringVar()
        self.color = tk.StringVar()
        self.adhar = tk.StringVar()
        self.licence = tk.StringVar()
        self.rc = tk.StringVar()
        self.pay_details = tk.StringVar()
        self.pay = tk.StringVar()

        self.register()
        
    def register_submit(self):
        with sqlite3.connect("parking.db") as db:
            cursur = db.cursor()
            register_user = ("INSERT INTO User VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            cursur.execute(register_user,[(self.new_id_f.get()),(self.new_id_f.get()),(self.new_first_name_f.get()),(self.new_last_name_f.get()),(self.phone_number_f.get()),(self.email_f.get()),(self.designation.get()),(self.Department_f.get()),(self.block_f.get()),(self.wheel.get()),(self.color_f.get()),(self.adhar_f.get()),(self.licence_f.get()),(self.rc_f.get()),(self.pay_details_f.get())])
            db.commit()
        db.close()
        messagebox.showinfo("Success", f"Record Succesfully Added!\n your password is {self.new_id_f.get()}")
        
        
    def text_r(self):
        value= self.pay_details.get()
        cost = "0"
        if value == '1 Month':
            cost = "1000"
        elif value == '6 Months':
            cost = "5500"
        elif value == '12 Months':
            cost = "10000"
        self.pay.set(cost)
        
    def register(self):
        self.rcanvas_data = tk.Canvas(self , width = 600 , height = 1000 , bd = 0 , highlightthickness = 2)
        self.rcanvas_data.grid(row=0,column=0)

        self.new_first_name_lbl = tk.Label(self.rcanvas_data , text = "First Name")
        self.new_first_name_lbl.grid(row = 0 , column = 0)
        
        self.new_first_name_f = tk.Entry(self.rcanvas_data , textvariable = self.first_name)
        self.new_first_name_f.grid(row = 0 , column = 1)

        self.new_last_name_lbl = tk.Label(self.rcanvas_data , text = "Last Name")
        self.new_last_name_lbl.grid(row = 1 , column = 0)
        
        self.new_last_name_f = tk.Entry(self.rcanvas_data , textvariable = self.last_name)
        self.new_last_name_f.grid(row = 1 , column = 1)
        
        self.new_id_lbl = tk.Label(self.rcanvas_data , text = "U.ID / Reg. no.")
        self.new_id_lbl.grid(row = 2 , column = 0)
        
        self.new_id_f = tk.Entry(self.rcanvas_data , textvariable = self.id)
        self.new_id_f.grid(row = 2 , column = 1)

        self.phone_number_lbl = tk.Label(self.rcanvas_data , text = "Phone number")
        self.phone_number_lbl.grid(row = 3 , column = 0)

        self.phone_number_f = tk.Entry(self.rcanvas_data , textvariable = self.phone_number)
        self.phone_number_f.grid(row = 3 , column = 1)

        self.email_lbl = tk.Label(self.rcanvas_data , text = "E-mail")
        self.email_lbl.grid(row = 4 , column = 0)

        self.email_f = tk.Entry(self.rcanvas_data , textvariable = self.email)
        self.email_f.grid(row = 4 , column = 1)

        self.designation_lbl = tk.Label(self.rcanvas_data , text = "Designation")
        self.designation_lbl.grid(row = 5 , column = 0)

        self.designation.set("none")

        self.designation_f = tk.OptionMenu(self.rcanvas_data , self.designation , "Student" , "Faculty")
        self.designation_f.grid(row = 5 , column = 1)

        self.Department = tk.Label(self.rcanvas_data , text = "Department")
        self.Department.grid(row = 6 , column = 0)

        self.Department_f = tk.Entry(self.rcanvas_data , textvariable = self.Department)
        self.Department_f.grid(row = 6 , column = 1)

        self.block = tk.Label(self.rcanvas_data , text = "Block")
        self.block.grid(row = 7 , column = 0)

        self.block_f = tk.Entry(self.rcanvas_data , textvariable = self.block)
        self.block_f.grid(row = 7 , column = 1)

        self.wheel.set("none")

        self.wheel_l = tk.Label(self.rcanvas_data , text = "choose your wheeler : ").grid(row=8 , column = 0)
        
        self.wheel_f = tk.OptionMenu(self.rcanvas_data , self.wheel , "2-wheeler" , "3-wheeler" , "4-wheeler" , "6-wheeler")
        self.wheel_f.grid(row = 8 , column = 1)
        
        self.color_lbl = tk.Label(self.rcanvas_data , text = "Vehicle Color")
        self.color_lbl.grid(row = 9 , column = 0)

        self.color_f = tk.Entry(self.rcanvas_data , textvariable = self.color)
        self.color_f.grid(row = 9 , column = 1)

        self.adhar_lbl = tk.Label(self.rcanvas_data , text = "Adhar Card Number")
        self.adhar_lbl.grid(row = 10 , column = 0)

        self.adhar_f = tk.Entry(self.rcanvas_data , textvariable = self.adhar)
        self.adhar_f.grid(row = 10 , column = 1)

        self.licence_lbl = tk.Label(self.rcanvas_data , text = "Licence Number")
        self.licence_lbl.grid(row = 11 , column = 0)

        self.licence_f = tk.Entry(self.rcanvas_data , textvariable = self.licence)
        self.licence_f.grid(row = 11 , column = 1)

        self.rc_lbl = tk.Label(self.rcanvas_data , text = "Reg. certification (RC)")
        self.rc_lbl.grid(row = 12 , column = 0)

        self.rc_f = tk.Entry(self.rcanvas_data , textvariable = self.rc)
        self.rc_f.grid(row = 12 , column = 1)

        self.pay_details.set("none")

        self.pay_l = tk.Label(self.rcanvas_data , text = "choose time frame of your subscription : ").grid(row=13 , column = 0)
        
        self.wheel_f = tk.OptionMenu(self.rcanvas_data , self.pay_details , "1 Month" , "6 Months" , "12 Months")
        self.wheel_f.grid(row = 13 , column = 1)

        
        self.pay_details_l = tk.Label(self.rcanvas_data , text = "Fee")
        self.pay_details_l.grid(row = 14 , column = 0)
        

        self.pay_details_f = tk.Entry(self.rcanvas_data ,state = "disabled" , textvariable = self.pay)
        self.pay_details_f.grid(row = 14 , column = 1)

        self.get = tk.Button(self.rcanvas_data , text = "get data" ,command = self.text_r).grid(row = 14 , column = 2)

        self.register_btn = tk.Button(self.rcanvas_data , text = "Register" , command = self.register_submit)
        self.register_btn.grid(row = 15 , column = 1)

        self.Index = tk.Button(self.rcanvas_data , text="Back to main" , command = lambda: self.controller.show_frame("Application"))
        self.Index.grid(column = 0 , row = 15)
        
        self.Index = tk.Button(self.rcanvas_data , text="Admin Register" , command = lambda: self.controller.show_frame("Register_Admin"))
        self.Index.grid(column = 3 , row = 15)
        
class Temporary_Parking(tk.Frame):

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.block = tk.StringVar()
        self.vehicle_no = tk.StringVar()
        self.id = tk.StringVar()
        self.vehicle_type = tk.StringVar()
        self.phn = tk.StringVar()
        self.email = tk.StringVar()
        self.vehicle_color = tk.StringVar()
        self.license = tk.StringVar()
        self.rc = tk.StringVar()
        self.entry_time = tk.StringVar()
        self.widget()
        
    def avail(self):
        with sqlite3.connect("parking.db") as db:  
            cursur = db.cursor()
            count = cursur.execute("select count(*)")  
            tempvar = cursur.fetchall()
            rowcount = len(tempvar)
            db.commit 
        db.close()
        a = 50 - rowcount
        messagebox.showinfo("", a)

    def register_s(self):
        with sqlite3.connect("parking.db") as db:
            cursur = db.cursor()
            temporary_user = ("INSERT INTO Log VALUES(?,?,?,?,?,?,?,?,?)")
            cursur.execute(temporary_user,[(self.block.get()),(self.vehicle_no.get()),(self.phn.get()),(self.email.get()),(self.vehicle_type.get()),(self.vehicle_color.get()),(self.license.get()),(self.rc.get()),(self.entry_time.get())])
            db.commit()
        db.close()
        messagebox.showinfo("Receipt", f"BLOCK:{self.block.get()}\nVEHICLE NO: {self.vehicle_no.get()}\nPHONE NO:{self.phn.get()}\nEMAIL: {self.email.get()}\nVEHICLE TYPE: {self.vehicle_type.get()}\nVEHICLE COLOR: {self.vehicle_color.get()}\nLICENCE NO: {self.license.get()}\nRC NO: {self.rc.get()}\nENTRY TIME: {self.entry_time.get()}") 

    def widget(self):
        self.canvas=tk.Canvas(self , width = 600, height = 1000 , bd = 0 , highlightthickness = 2)
        self.canvas.grid(row=0,column=0)
        
        self.block_l = tk.Label (self.canvas , text = "BLOCK: ")
        self.block_l.grid(row = 0 , column = 0)
        
        self.new_block=tk.Entry(self.canvas, bd=5, textvariable = self.block)
        self.new_block.grid(row = 0 , column = 1)
        
        self.Vehicleno = tk.Label (self.canvas, text="VEHICLE NO.: ")
        self.Vehicleno.grid (row = 1 , column = 0)
        
        self.new_Vehicle_no = tk.Entry (self.canvas, bd=5, textvariable = self.vehicle_no)
        self.new_Vehicle_no.grid (row = 1 , column = 1)
        
        self.Vcolour=tk.Label(self.canvas,text= "VEHICLE COLOR: ")
        self.Vcolour.grid(row = 2 , column = 0)
        
        self.new_vehicle_color = tk.Entry (self.canvas, bd=5, textvariable = self.vehicle_color )
        self.new_vehicle_color.grid (row = 2, column = 1)

        self.wheel = tk.Label(self.canvas , text = " wheeler type : ").grid(row=3 , column = 0)
        
        self.vehicletype = tk.OptionMenu(self.canvas , self.vehicle_type , "2-wheeler" , "3-wheeler" , "4-wheeler" , "6-wheeler")
        self.vehicletype.grid(row = 3 , column = 1)
        
        self.Lno = tk.Label (self.canvas, text= "LICENSE NO: ")
        self.Lno.grid (row = 4 , column = 0)
        
        self.new_license = tk.Entry (self.canvas, bd=5, textvariable = self.license)
        self.new_license.grid (row = 4 , column = 1)
        
        self.RCno = tk.Label (self.canvas, text= "RC NO: ")
        self.RCno.grid (row = 5 , column = 0)
        
        self.new_rc = tk.Entry (self.canvas, bd=5,textvariable = self.rc)
        self.new_rc.grid (row = 5 , column = 1)
        
        self.entryt=tk.Label (self.canvas, text= "ENTRY TIME: ")
        self.entryt.grid (row = 6, column = 0)
        
        self.new_entry_time = tk.Entry (self.canvas, bd=5, textvariable = self.entry_time)
        self.new_entry_time.grid (row = 6 , column = 1)
        
        self.Phno = tk.Label (self.canvas, text = "PHN NO: ")
        self.Phno.grid (row = 7 , column = 0)
        
        self.Phone_number = tk.Entry (self.canvas, bd=5 ,textvariable = self.phn)
        self.Phone_number.grid (row = 7 , column = 1)
        
        self.Emailid = tk.Label (self.canvas, text = "Email ID: ")
        self.Emailid.grid (row = 8 , column = 0)
        
        self.new_email = tk.Entry (self.canvas, bd=5, textvariable = self.email)
        self.new_email.grid (row = 8 , column = 1)
        
        self.submit = tk.Button (self.canvas, text="SUBMIT", command = self.register_s)
        self.submit.grid (row = 10 , column = 1)

        self.Index = tk.Button(self.canvas , text="Exit" , command = lambda: self.controller.show_frame("Application"))
        self.Index.grid (row = 10 , column = 0)
        
        self.avail = tk.Button(self.canvas , text="Availabilty" , command = self.avail)
        self.avail.grid (row = 10 , column = 2)
        
class Feedback(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.message = tk.StringVar()
        self.widget()

    def register_s(self):
        messagebox.showinfo(" ","Thanks for the feedack!!") 
        

    def widget(self):
        self.canvas=tk.Canvas(self , width = 600, height = 1000 , bd = 0 , highlightthickness = 2)
        self.canvas.grid(row=0,column=0)
        
        self.name_l = tk.Label (self.canvas , text = "Name: ")
        self.name_l.grid(row = 0 , column = 0)
        
        self.new_name = tk.Entry(self.canvas, bd=5, textvariable = self.name)
        self.new_name.grid(row = 0 , column = 1)
        
        self.email = tk.Label (self.canvas, text="Email: ")
        self.email.grid (row = 1 , column = 0)
        
        self.new_email = tk.Entry (self.canvas, bd=5, textvariable = self.email)
        self.new_email.grid (row = 1 , column = 1)
        
        self.message = tk.Label(self.canvas,text= "Message: ")
        self.message.grid(row = 2 , column = 0)
        
        self.new_vehicle_color = tk.Entry (self.canvas, bd=5, textvariable = self.message)
        self.new_vehicle_color.grid (row = 2, column = 1)

        self.submit = tk.Button (self.canvas, text="SUBMIT", command = self.register_s)
        self.submit.grid (row = 10 , column = 1)

        self.Index = tk.Button(self.canvas , text="Exit" , command = lambda: self.controller.show_frame("Application"))
        self.Index.grid (row = 10 , column = 0)
        
class Register_Admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.name = tk.StringVar()
        self.id = tk.StringVar()
        self.password = self.id.get()
        self.register()
        
    def register_submit(self):
        with sqlite3.connect("parking.db") as db:
            cursur = db.cursor()
            register_user= ("INSERT INTO User VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
            cursur.execute(register_user,[(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get()),(self.new_id_f.get())])
            db.commit()
        db.close()
        messagebox.showinfo("Success", f"Record Succesfully Added!\n your password is {self.new_id_f.get()}")
        
        
    def register(self):
        self.rcanvas_data = tk.Canvas(self , width = 600 , height = 1000 , bd = 0 , highlightthickness = 2)
        self.rcanvas_data.grid(row=0,column=0)

        self.new_id_lbl = tk.Label(self.rcanvas_data , text = "Admin ID")
        self.new_id_lbl.grid(row = 0 , column = 0)
        
        self.new_id_f = tk.Entry(self.rcanvas_data , textvariable = self.id)
        self.new_id_f.grid(row = 0 , column = 1)
        
        self.new_password_lbl = tk.Label(self.rcanvas_data , text = "Password")
        self.new_password_lbl.grid(row = 1 , column = 0)
        
        self.new_password_f = tk.Entry(self.rcanvas_data , textvariable = self.password)
        self.new_password_f.grid(row = 1 , column = 1)

        self.register_btn = tk.Button(self.rcanvas_data , text = "Register" , command = self.register_submit)
        self.register_btn.grid(row = 2 , column = 0)

        self.Index = tk.Button(self.rcanvas_data , text="Back to main" , command = lambda: self.controller.show_frame("Application"))
        self.Index.grid(column = 1 , row = 2)

        
if __name__ == "__main__":
    
    app = SampleApp()
    app.mainloop()