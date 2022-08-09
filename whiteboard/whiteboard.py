from tkinter import *
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk



root = Tk()
root.title ("white Board")
root.state("zoomed")
#root.geometry("1100x750+150+40")
root.configure (bg="#f2f3f5")
root.resizable (False, False)

current_x =0
current_y=0
color ='black'


def locate_xy(work):
    global current_x, current_y
    current_x =work.x
    current_y =work.y


def addLine(work):
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth=TRUE)
    current_x,current_y =work.x,work.y


def show_color(new_color):
    global color
    color =new_color



def new_canvas():
    canvas.delete('all')
    display_pallete()

#icon
image_icon =PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#color_box=PhotoImage(file="color section.png")

#Label(root,image=color_box,bg="#f2f3f5").place(x=10,y=20)

eraser=PhotoImage(file="jattdieraser.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=30,y=735)
colors=Canvas (root,bg="#ffffff",width=70,height=710,bd=0)
colors.place(x=10,y=10)

def display_pallete():
    id=colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    id=colors.create_rectangle((10,40,30,60),fill='gray')
    colors.tag_bind(id,'<Button-1>',lambda x:  show_color('gray'))


    id=colors.create_rectangle((10,70,30,90),fill='brown4')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown4'))

    id=colors.create_rectangle((10,100,30,120),fill='red')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

    id=colors.create_rectangle((10,130,30,150),fill='orange')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))

    id=colors.create_rectangle((10,160,30,180),fill='yellow')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))

    id=colors.create_rectangle((10,190,30,210),fill='green')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

    id=colors.create_rectangle((10,220,30,240),fill='blue')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

    id=colors.create_rectangle((10,250,30,270),fill='purple')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))
    id=colors.create_rectangle((10,280,30,300),fill='pink')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('pink'))
    id=colors.create_rectangle((10,310,30,330),fill='cyan')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('cyan'))
    id=colors.create_rectangle((10,340,30,360),fill='tan')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('tan'))

    id=colors.create_rectangle((10,370,30,390),fill='olive')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('olive'))

    id=colors.create_rectangle((10,400,30,420),fill='yellow2')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow2'))

    id=colors.create_rectangle((10,430,30,450),fill='violetred4')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('violetred4'))

    id=colors.create_rectangle((10,460,30,480),fill='violet')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('violet'))

    id=colors.create_rectangle((10,490,30,510),fill='dodgerblue1')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('dodgerblue1'))

    id=colors.create_rectangle((10,520,30,540),fill='tomato3')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('tomato3'))

    id=colors.create_rectangle((10,550,30,570),fill='tomato1')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('tomato1'))

    id=colors.create_rectangle((10,580,30,600),fill='thistle2')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('thistle2'))

    id=colors.create_rectangle((10,610,30,630),fill='tan4')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('tan4'))

    id=colors.create_rectangle((10,640,30,660),fill='steelblue4')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('steelblue4'))

    id=colors.create_rectangle((10,670,30,690),fill='steelblue1')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('steelblue1'))


    #right colours


    id=colors.create_rectangle((40,10,60,30),fill='aliceblue')
    colors.tag_bind(id,'<Button>',lambda x: show_color('aliceblue'))

    id=colors.create_rectangle((40,40,60,60),fill='springgreen')
    colors.tag_bind(id,'<Button>',lambda x: show_color('springgreen'))

    id=colors.create_rectangle((40,70,60,90),fill='snow3')
    colors.tag_bind(id,'<Button>',lambda x: show_color('snow3'))

    id=colors.create_rectangle((40,100,60,120),fill='slateblue1')
    colors.tag_bind(id,'<Button>',lambda x: show_color('slateblue1'))

    id=colors.create_rectangle((40,130,60,150),fill='skyblue1')
    colors.tag_bind(id,'<Button>',lambda x: show_color('skyblue1'))

    id=colors.create_rectangle((40,160,60,180),fill='dodgerblue1')
    colors.tag_bind(id,'<Button>',lambda x: show_color('dodgerblue1'))

    id=colors.create_rectangle((40,190,60,210),fill='magenta')
    colors.tag_bind(id,'<Button>',lambda x: show_color('magenta'))



    id=colors.create_rectangle((40,220,60,240),fill='seagreen1')
    colors.tag_bind(id,'<Button>',lambda x: show_color('seagreen1'))

    id=colors.create_rectangle((40,250,60,270),fill='salmon1')
    colors.tag_bind(id,'<Button>',lambda x: show_color('salmon1'))

    id=colors.create_rectangle((40,280,60,300),fill='royalblue3')
    colors.tag_bind(id,'<Button>',lambda x: show_color('royalblue3'))

    id=colors.create_rectangle((40,310,60,330),fill='rosybrown2')
    colors.tag_bind(id,'<Button>',lambda x: show_color('rosybrown2'))

    id=colors.create_rectangle((40,340,60,360),fill='olive')
    colors.tag_bind(id,'<Button>',lambda x: show_color('olive'))

    id=colors.create_rectangle((40,370,60,390),fill='purple3')
    colors.tag_bind(id,'<Button>',lambda x: show_color('purple3'))

    id=colors.create_rectangle((40,400,60,420),fill='purple')
    colors.tag_bind(id,'<Button>',lambda x: show_color('purple'))

    id=colors.create_rectangle((40,430,60,450),fill='plum')
    colors.tag_bind(id,'<Button>',lambda x: show_color('plum'))

    id=colors.create_rectangle((40,460,60,480),fill='gold')
    colors.tag_bind(id,'<Button>',lambda x: show_color('gold'))

    id=colors.create_rectangle((40,490,60,510),fill='palevioletred1')
    colors.tag_bind(id,'<Button>',lambda x: show_color('palevioletred1'))

    id=colors.create_rectangle((40,520,60,540),fill='navy')
    colors.tag_bind(id,'<Button>',lambda x: show_color('navy'))

    id=colors.create_rectangle((40,550,60,570),fill='navajowhite4')
    colors.tag_bind(id,'<Button>',lambda x: show_color('navajowhite4'))

    id=colors.create_rectangle((40,580,60,600),fill='deeppink1')
    colors.tag_bind(id,'<Button>',lambda x: show_color('deeppink1'))

    id=colors.create_rectangle((40,610,60,630),fill='crimson')
    colors.tag_bind(id,'<Button>',lambda x: show_color('crimson'))

    id=colors.create_rectangle((40,640,60,660),fill='darkgoldenrod4')
    colors.tag_bind(id,'<Button>',lambda x: show_color('darkgoldenrod4'))

    id=colors.create_rectangle((40,670,60,690),fill='khaki')
    colors.tag_bind(id,'<Button>',lambda x: show_color('khaki'))



display_pallete()



canvas=Canvas(root,width=1435,height=770,background="white",cursor="hand2")
canvas.place(x=90,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addLine)


###########slider########3

current_value =tk.DoubleVar()
def get_current_value():
    return'{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())
slider =ttk.Scale(root,from_=0,to=1000,orient='horizontal',command=slider_changed,variable=current_value)
slider.place(x=30,y=800)

#value label
value_label =ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=820 )



root.mainloop()