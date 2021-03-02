# Creating a database management software

import tkinter
from tkinter import *
import tkinter.messagebox
class databaseApplication:
    def __init__ (self):
        self.main_window = tkinter.Tk()

        #Setting width and height
        self.main_window.geometry("500x500")

        #Setting title for program
        self.main_window.title('Database Management Project')

        #Setting the title icon for program

        #self.main_window.wm_iconbitmap('logo.png')

        #Setting background color for program
        self.main_window.configure(background='green')
        #Label in database registration heading
        self.headingFrame = tkinter.Frame(self.main_window)
        self.heading = tkinter.Label(self.headingFrame, fg='blue', font='courier 30 bold', text='Registration Form', justify='center',)

        self.heading.pack(side='top')
        self.headingFrame.pack(pady='10', ipadx='10')
        
        #Creating a Frame Box for Entering labels
        self.topFrame = tkinter.Frame(self.main_window)
        self.bottomFrame = tkinter.Frame(self.main_window)

        self.password = tkinter.Frame(self.main_window)

        self.password_label = tkinter.Label(self.password, text='Enter your password: ', fg='blue', font='serif 10 bold')
        self.password_label.pack(side='left')

        self.password_frame = tkinter.Entry(self.password, width=18)
        self.password_frame.pack(side='left')
        self.password.pack(pady='10')

        self.name = tkinter.Label(self.topFrame, text='Enter your name: ', fg='blue', font='serif 10 bold')
        self.name_box = tkinter.Entry(self.topFrame, width=18)
        self.phone_number = tkinter.Label(self.bottomFrame, text='Enter your phone number: ', fg='blue', font='serif 10 bold')
        self.phoneNumber_box = tkinter.Entry(self.bottomFrame, width=18)

        self.name.pack(side='left', padx='10')
        self.phone_number.pack(side='left')

        self.name_box.pack(side='left')
        self.phoneNumber_box.pack(side='left')
        #Packing frame 
        self.topFrame.pack(pady='10', ipadx='10')
        self.bottomFrame.pack(pady='10', ipadx='10')

        self.buttonFrame = tkinter.Frame(self.main_window)

        self.submit = tkinter.Button(self.buttonFrame, text='Submit', font='serif 15 bold')
        self.submit.pack(pady='10', ipadx='10')
        self.buttonFrame.pack(pady='10', ipadx='10')

    #Setting StringVar for variables
        tkinter.mainloop()

application = databaseApplication()