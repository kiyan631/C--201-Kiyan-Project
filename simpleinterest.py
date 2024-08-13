from tkinter import *
window=Tk()



window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


def calculate_interest():

     p  = float(principle.get())
     r  = float(rate.get())
     t  = float(time.get())
     i  = (p*r*t)/100
     interest = round(i,2)
     name = username.get()

     result_label.destroy()

     








     output_message=Label(result_frame,text=name+", Your simple interest is  "+str(interest), bg = "lightcyan", font=("Calibri", 12), width=42)
     output_message.place(x=20,y=40)
     output_message.pack()


app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50,y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20,y=90)


username = Entry(window,text="",bd=2,width=22)
username.place(x=190,y=90)


principle_label=Label(window, text="Enter principle (rupees)", fg = "black", bg = "lightcyan", font=("Calibri", 12))
principle_label.place(x=20,y=135)



principle=Entry(window, text="", bd=2, width=15)
principle.place(x=190, y=145)



rate_label=Label(window, text="Enter Rate of Interest (%)", fg = "black", bg = "lightcyan", font=("Calibri", 12))
rate_label.place(x=20, y=185)


rate=Entry(window, text="", bd=2, width=15)
rate.place(x=190, y=225)



time_label=Label(window, text="Enter time (Yrs)", fg = "black", bg = "lightcyan", font=("Calibri", 12))
time_label.place(x=20,y=235)


time=Entry(window, text="", bd=2, width=15)
time.place(x=190, y=190)



calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_interest)
calculate_button.place(x=20,y=270)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()




































window.mainloop()
