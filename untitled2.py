import tkinter as tk

window = tk.Tk()

window.title("我的第一個ＧＵI程式")

window.geometry('500x500')

import tkinter.messagebox

def clickMe():
    tkinter.messagebox.showinfo(title='提示',message='好痛')
label = tk.Label(window,text="我的GUI",bg="#00FF00",fg="#FF00FF")
label.pack()

entry = tk.Entry(window,width = 20)
entry.pack()

button = tk.Button(window,text = "按鈕",command = clickMe)
button.pack()

window.mainloop()

