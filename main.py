from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import qrcode
import pyttsx3

class APP:
    def __init__(self,master):

            #creating a style
            master.title('Fastshare')
            master.resizable(False,False)
            master.configure(background='#2ef2ae')
            #master.geometry("400x420")



            self.style=ttk.Style()
            self.style.configure('TFrame',background='#fffb00')
            #self.style.configure('header.TLabel',background='#ff1c8a')
            self.style.configure('TLabel', background='#ecf02b')
            self.style.configure('header.TLabel',background='#fffb00')
            self.style.configure('btn.TButton',background='#1cff99',activebackground='orange')
            self.style.configure('design.TLabel',background='#fc123d',foreground='#2ef2ae')
            # creating header frame work

            self.frame_header=ttk.Frame(master,relief=RIDGE)
            self.frame_header.pack()

            self.logo = PhotoImage(file="download.gif")
            ttk.Label(self.frame_header,image=self.logo,style='header.TLabel',background='#fc0000',borderwidth=12).grid(row=0,column=0,rowspan=2)
            ttk.Label(self.frame_header,text="FASTSHARE!",font=('Arial',14,'bold'),background='#e6e20b',foreground='red').grid(row=0,column=1)
            ttk.Label(self.frame_header,wraplength=300,style='header.TLabel',text = ("This app allows you to share u details! ."
                          "It shares your info by QR code!!." "BE Free to fill the form it doent take into our data base!"),
                  font=('Arial',10)).grid(row=1,column=1,columnspan=2)
            ttk.Label(self.frame_header,text="-------------------------------------------------------------------------",style='design.TLabel').grid(columnspan=2)
             #creating body of the cotent

            self.frame_body=ttk.Frame(master,relief=SUNKEN)
           # self.notebook.add(self.frame_body,text="page 1")
            self.frame_body.pack()

            ttk.Label(self.frame_body,text="Name:").grid(row=0,column=0,sticky='w',padx=6,pady=4)
            ttk.Label(self.frame_body, text="Age:").grid(row=0, column=1, sticky='w', padx=6)
            ttk.Label(self.frame_body, text="Dob:").grid(row=2, column=0, sticky='w', padx=6)
            ttk.Label(self.frame_body, text="City:").grid(row=2, column=1, sticky='w', padx=6)
            ttk.Label(self.frame_body, text="State:").grid(row=4, column=0, sticky='w', padx=6)
            ttk.Label(self.frame_body, text="Pincode:").grid(row=4, column=1, sticky='w', padx=6)
            ttk.Label(self.frame_body, text="Aadhar card NO:").grid(row=6, column=0, sticky='w', padx=6)
            ttk.Label(self.frame_body, text="Pan card no:").grid(row=6, column=1, sticky='w', padx=6)
            ttk.Label(self.frame_body, text="Driving licence no:").grid(row=8, column=0, sticky='w', padx=6)
            ttk.Label(self.frame_body, text="Qualifications:").grid(row=8, column=1, sticky='w', padx=6)


             #creating a entry

            self.entry_name=ttk.Entry(self.frame_body,width=20,font=('Arial',10,'bold'))
            self.entry_age = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'italic'))
            self.entry_dob = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'italic'))
            self.entry_city = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'bold'))
            self.entry_state = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'bold'))
            self.entry_pincode = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'italic'))
            self.entry_aadhar = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'italic'))
            self.entry_pancard = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'bold'))
            self.entry_driving = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'bold'))
            self.entry_qualifications = ttk.Entry(self.frame_body, width=20, font=('Arial', 10, 'bold'))

             #griding the entry

            self.entry_name.grid(row=1, column=0, padx=5, pady=7)
            self.entry_age.grid(row=1, column=1, padx=5, pady=7)
            self.entry_dob.grid(row=3, column=0, padx=5, pady=7)
            self.entry_city.grid(row=3, column=1, padx=5, pady=7)
            self.entry_state.grid(row=5, column=0, padx=5, pady=7)
            self.entry_pincode.grid(row=5, column=1, padx=5, pady=7)
            self.entry_aadhar.grid(row=7, column=0, padx=5, pady=7)
            self.entry_pancard.grid(row=7, column=1, padx=5, pady=7)
            self.entry_driving.grid(row=9, column=0, padx=5, pady=7)
            self.entry_qualifications.grid(row=9, column=1, padx=5, pady=7)

            #insertin something
            self.entry_qualifications.insert(0,"Eg.BCA,B.Tech....")
            self.entry_dob.insert(0, "dd.mm.yyyy")
            self.entry_aadhar.insert(0, "XXXX YYYY ZZZZ")
            self.entry_name.insert(0, "V.Rahul...")
            self.entry_age.insert(0, "23")
            self.entry_pancard.insert(0, "ZZZZZZ")
            self.entry_pincode.insert(0, "XXXXXXXX")
            self.entry_driving.insert(0, "QQQQQ")



            #creating a entry keyborad for user
            self.entry_name.bind("<Return>",self.return_)
            self.entry_age.bind("<Return>", self.return_)

             #creating button

            ttk.Button(self.frame_body,text="Clear",command=self.clear,style='btn.TButton').grid(row=10,column=0,padx=5,pady=7,sticky='w')
            self.qrbtn =ttk.Button(self.frame_body,text="Show QR",command=self.qrcodeviwer,style='btn.TButton').grid(row=10,column=1,padx=5,pady=7,sticky='e')
            ttk.Button(self.frame_body, text="Sumbit", command=self.sumbit, style='btn.TButton').grid(row=10, column=0,
                                                                                                      padx=5, pady=7,
                                                                                                      sticky='e')
            self.speak_1()

    def speak_1(self):
        self.engine=pyttsx3.init()
        self.engine.say("Hello user welcome to the fast share!,Please begin with clear command and write in the format.")
        self.engine.runAndWait()

    def speak_2(self):
        self.engine=pyttsx3.init()
        self.engine.say("Thank you for filling this form!,You can view your data's by scanning the qr code!")
        self.engine.runAndWait()
    def qrcodeviwer(self):
        # creating a top level window
            self.window = Toplevel(background='#f50217')
            self.window.title("QR CODE")
            self.img=PhotoImage(file="test.jpg").subsample(2,2)
            ttk.Label(self.window,image=self.img,background='#fc0000').pack()

    def return_(self,event):
            print("enter pressed")


    #using the button
    def sumbit(self):
        self.val=1
        print("Name:{}".format(self.entry_name.get()))
        print("Age:{}".format(self.entry_age.get()))
        print("Dob:{}".format(self.entry_dob.get()))
        print("City:{}".format(self.entry_city.get()))
        print("State:{}".format(self.entry_state.get()))
        print("Pincode:{}".format(self.entry_pincode.get()))
        #if self.val == 1:
         #   self.qrbtn.config(text="get qr")

        #creating a qr code
        self.q = ["Name:{}".format(self.entry_name.get()), "Age:{}".format(self.entry_age.get()),
                  "Dob:{}".format(self.entry_dob.get()), "City:{}".format(self.entry_city.get())
            , "State:{}".format(self.entry_state.get()), "Pincode:{}".format(self.entry_pincode.get()),
                  "Aaadhar Card no:{}".format(self.entry_aadhar.get()),
                  "Pan card:{}".format(self.entry_pancard.get()), "Driving Licence:{}".format(self.entry_driving.get()),
                  "Qualifications:{}".format(self.entry_qualifications.get())]
        print(self.q)
        self.r = qrcode.make(self.q)
        self.r.save("test.jpg")

        #calling the speak function
        self.speak_2()

        self.clear()
        messagebox.showinfo(title="Succesful",message="Your sumbision is succesfull! and QR code is generated!")
    def clear(self):
        self.entry_name.delete(0,'end')
        self.entry_age.delete(0,'end')
        self.entry_dob.delete(0,'end')
        self.entry_city.delete(0,'end')
        self.entry_state.delete(0,'end')
        self.entry_pincode.delete(0,'end')
        self.entry_pancard.delete(0, 'end')
        self.entry_aadhar.delete(0, 'end')
        self.entry_driving.delete(0, 'end')
        self.entry_qualifications.delete(0, 'end')

def main():
    root=Tk()
    app=APP(root)
    root.mainloop()

if __name__ == "__main__": main()
