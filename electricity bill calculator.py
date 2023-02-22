from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()

GUI.title('โปรแกรมคำนวณค่าไฟฟ้า')
GUI.geometry('500x400')

L1 = Label(GUI,text='โปรแกรมคำนวณค่าไฟฟ้าของแต่ละอุปกรณ์',font=('Angsana Nwe',18),fg='green')
L1.place(x=30,y=20)


#ช่องกรอกกำลังไฟฟ้า
FB1 = Frame(GUI)
FB1.place(x=20,y=80)
B1 = Label(FB1,text='วัตต์',font=('Angsana Nwe',12),fg='black')
B1.pack(ipadx=20,ipady=20)
FB2 = Frame(GUI)
FB2.place(x=100,y=100)
tB1 = Entry(FB2,font=('Angsana Nwe',12),fg='black')
tB1.pack(ipadx=1,ipady=1)
#Label(text='วัตต์',padx=30, pady=60,font=('Angsana New',16)).grid(row=0,sticky=W)

#ช่องกรอกชั่วโมงการทำงานของอุปกรณ์ไฟฟ้า
FB3 = Frame(GUI)
FB3.place(x=20,y=125)
B2 = Label(FB3,text='ชั่วโมง',font=('Angsana Nwe',12),fg='black')
B2.pack(ipadx=20,ipady=20)
FB4 = Frame(GUI)
FB4.place(x=100,y=145)
tB2 = Entry(FB4,font=('Angsana Nwe',12),fg='black')
tB2.pack(ipadx=1,ipady=1)


#วันทำงานของอุปกร์ไฟฟ้า
FB5 = Frame(GUI)
FB5.place(x=20,y=170)
B3 = Label(FB5,text='วันทำงาน',font=('Angsana Nwe',12),fg='black')
B3.pack(ipadx=20,ipady=20)
FB6 = Frame(GUI)
FB6.place(x=100,y=190)
tB3 = Entry(FB6,font=('Angsana Nwe',12),fg='black')
tB3.pack(ipadx=1,ipady=1)

#บาทต่อยูนิต
FB7 = Frame(GUI)
FB7.place(x=20,y=220)
B4 = Label(FB7,text='บาท/หน่วย',font=('Angsana Nwe',12),fg='black')
B4.pack(ipadx=20,ipady=20)
FB8 = Frame(GUI)
FB8.place(x=100,y=240)
tB4 = Entry(FB8,font=('Angsana Nwe',12),fg='black')
tB4.pack(ipadx=1,ipady=1)

#การคำนวณ
def Button1():
    w = tB1.get()
    w2 = int(w) / 1000
    h = tB2.get()
    h2 = int(h)
    d = tB3.get()
    d2 = int(d)
    Ub = tB4.get()
    Ub2 = int(Ub)

    PWE = w2 * h2 * d2
    UPE = PWE * Ub2 
    text1 = 'บาท/หน่วย' 
    messagebox.showinfo('ค่ายูนิตไฟฟ้า',str(UPE)+ text1)

#ปุ่มคำนวณ
FB9 = Frame(GUI)
FB9.place(x=200,y=270)
B2 = ttk.Button(FB9,text='คำนวณ',command=Button1)
B2.pack(ipadx=5,ipady=5)


GUI.mainloop()