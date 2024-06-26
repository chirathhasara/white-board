from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root= Tk()
root.title("white board")
root.geometry('800x500+500+50')
root.resizable(False,False)

current_x,current_y=0,0
color='black'

def locate_xy(work):
    global current_x,current_y
    current_x=work.x
    current_y=work.y


def show_color(new_color):
    global color
    color=new_color


def addLine(work):
    global current_x,current_y
    global current_value
    size=current_value.get()
    canvas.create_oval((current_x-size,current_y-size,work.x+size,work.y+size),fill=color,outline='')
    current_x=work.x
    current_y=work.y

def new_canva():
    canvas.delete("all")
    panal_colors()


logo=PhotoImage(file="logo.png")
color_panal=PhotoImage(file='panal.png')
ereser=PhotoImage(file="eraser1.png")
ereser=ereser.subsample(8,8)
root.iconphoto(False,logo)

Label(root,image=color_panal,).place(x=10,y=10)
Button(root,image=ereser,bg='red',command=new_canva).place(x=50,y=380)

colors=Canvas(root,bg="white",width=60,height=330)
colors.place(x=35,y=30)
canvas=Canvas(root,bg="white",width=600,height=430,cursor='hand2')
canvas.place(x=150,y=10)

canvas.bind("<Button-1>",locate_xy)
canvas.bind("<B1-Motion>",addLine)


def panal_colors():
    id=colors.create_rectangle((15,10,50,45),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("black"))

    id=colors.create_rectangle((15,40,50,75),fill='red')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("red"))

    id=colors.create_rectangle((15,70,50,105),fill='yellow')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("yellow"))

    id=colors.create_rectangle((15,100,50,135),fill='green')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("green"))

    id=colors.create_rectangle((15,130,50,165),fill='blue')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("blue"))

    id=colors.create_rectangle((15,160,50,195),fill='purple')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("purple"))

    id=colors.create_rectangle((15,190,50,225),fill='brown')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("brown"))

    id=colors.create_rectangle((15,220,50,255),fill='gray')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("gray"))

    id=colors.create_rectangle((15,250,50,285),fill='cyan')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("cyan"))

    id=colors.create_rectangle((15,280,50,315),fill='orange')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color("orange"))

panal_colors()

current_value=tk.DoubleVar()
slider=ttk.Scale(root,from_=0,to=100,variable=current_value)
slider.place(x=30,y=450)

value_lable=ttk.Label(root,textvariable=current_value)
value_lable.place(x=30,y=475)

root.mainloop()