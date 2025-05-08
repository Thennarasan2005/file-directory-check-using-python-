import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title('filedirectory_checking desktop')
l=tk.Label(root,text='File Operation',font=('Arial black',25,'italic','bold'),justify=tk.CENTER)
l.pack()
l2=tk.Label(root,text='file:',font=('Arial black',25,'italic','bold'))
l2.place(x=50,y=200)
f_name=tk.StringVar()
e1=tk.Entry(root,textvariable=f_name,font=('Arial black',25,'italic','bold'))
e1.place(x=350,y=200)
def search():
    try:
        with open(f_name.get(),'r') as f:
            messagebox.showinfo('success','file found')
    except FileNotFoundError as err:
        messagebox.showwarning('error','file directory not found')

b=tk.Button(root,text='search',font=('arial black',25,'italic','bold'),command=search)
b.place(x=300,y=400)
root.mainloop()