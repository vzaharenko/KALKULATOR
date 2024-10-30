from tkinter import *
def plus():
    sk1 = (float(ent1.get()))
    sk2 = (float(ent2.get()))
    saskait = sk1 + sk2
    tex.config(bg="yellow",text = str(saskait))

def minus():
    sk1 = (float(ent1.get()))
    sk2 = (float(ent2.get()))
    atņemt = sk1 - sk2
    tex.config(bg="yellow",text = str(atņemt))

def reiz():
    sk1 = (float(ent1.get()))
    sk2 = (float(ent2.get()))
    reiz = sk1 * sk2
    tex.config(bg="yellow",text = str(reiz))

def dal():
    sk1 = (float(ent1.get()))
    sk2 = (float(ent2.get()))
    dal = sk1 / sk2
    tex.config(bg="yellow",text = str(dal))


wind= Tk()
wind.geometry('400x300+500+200')
wind.title('Aprēķini')

tex= Label(wind, font= 20, width=20, text='Ievadiet divus skaitļus')
tex.pack()

ent1 = Entry(wind,width=30)
ent1.pack()
ent2= Entry(wind, width=30)
ent2.pack()

btn1 = Button(wind,width=20, text='SaskaitIt', command=plus)
btn1.pack()

btn2 = Button(wind,width=20, text='Atņemt', command=minus)
btn2.pack()

btn3 = Button(wind,width=20, text='Reizināt', command=reiz)
btn3.pack()

btn4 = Button(wind,width=20, text='Dalīt', command=dal)
btn4.pack()


wind.mainloop()