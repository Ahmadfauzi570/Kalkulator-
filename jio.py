from tkinter import*

window =Tk()

def tombol_klik(item):
	global expression
	expression=expression +str(item)
	input_text.set (expression)

def bt_clear():
	global expression
	expression = ""
	input_text.set("")
	
def bt_equal():
	global expression
	result = str(eval(expression))
	input_text.set(result)
	expression = ""
	
expression= ""
input_text=StringVar()

frame1 = Frame(window,bg="pink", width=500, height=300)
frame1.pack(padx=20, pady=20)

frame2 = Frame(window,bg="black", width=500,height=300)
frame2.pack(padx=20,pady=30)

label= Label(frame1, text="Hello, ini adalah Label di Tkinter!")
label.pack(padx=20, pady=20)

label2 = Label (frame1, text ="Halo, ini Ahmad fauzi XII PPLG 1",textvariable=input_text)
label2 .pack(padx=20, pady=20)

button1 = Button(frame2, text="C",command=lambda:bt_clear(),width=10,bg="green",fg="black")
button1.grid(row=1,column=1,columnspan=2, pady= 20, padx = 20)


button3 = Button(frame2, text="/",command=lambda:tombol_klik("/"),bg="grey",fg="green")
button3.grid(row=1,column=3, pady= 20, padx = 20)

button4 = Button(frame2, text="*",command=lambda:tombol_klik("*"),
bg="grey",fg="white")
button4.grid(row=1,column=4, pady= 20, padx = 20)

button5= Button(frame2, text="7",command=lambda:tombol_klik("7"))
button5.grid(row=2,column=1, pady= 20, padx = 20)

button6= Button(frame2, text="8",command=lambda:tombol_klik("8"))
button6.grid(row=2,column=2, pady= 20, padx = 20)

button7= Button(frame2, text="9",command=lambda:tombol_klik("9"))
button7.grid(row=2,column=3, pady= 20, padx = 20)

button8= Button(frame2, text="+",
bg="grey",fg="white",command=lambda:tombol_klik("+"))
button8.grid(row=2,column=4, pady= 20, padx = 20)

button9= Button(frame2, text="4",command=lambda:tombol_klik("4"))
button9.grid(row=3,column=1, pady= 20, padx = 20)

button10= Button(frame2, text="5",command=lambda:tombol_klik("5"))
button10.grid(row=3,column=2, pady= 20, padx = 20)

button11= Button(frame2, text="6",command=lambda:tombol_klik("6"))
button11.grid(row=3,column=3, pady= 20, padx = 20)

button12= Button(frame2, text="-",
bg="grey",fg="white",command=lambda:tombol_klik("-"))
button12.grid(row=3,column=4, pady= 20, padx = 20)

button13= Button(frame2, text="1",command=lambda:tombol_klik("1"))
button13.grid(row=4,column=1, pady= 20, padx = 20)

button14= Button(frame2, text="2",command=lambda:tombol_klik("2"))
button14.grid(row=4,column=2, pady= 20, padx = 20)

button15= Button(frame2, text="3",command=lambda:tombol_klik("3"))
button15.grid(row=4,column=3, pady= 20, padx = 20)

button16= Button(frame2, text="=",command=lambda:bt_equal(),height=5,
bg="grey",fg="white")
button16.grid(row=4,column=4,rowspan=2, pady= 20, padx = 20)

button17= Button(frame2, text="0",width=10,command=lambda:tombol_klik("0"))
button17.grid(row=5,column=1, columnspan=2, pady= 20, padx = 20)

button19= Button(frame2, text=".",command=lambda:tombol_klik("."))
button19.grid(row=5,column=3, pady= 20, padx = 20)


window.mainloop()