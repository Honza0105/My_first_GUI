from tkinter import *
from time import sleep
def velocity(s, t):
    
    v = s / t
    return(v,'km/h')

def distance(v, t):
    
    s = v * t,
    return(s, 'km')

def time(s, v):
    
    t = s / v
    return(t, 'h')
def clicked_velocity():
    lbl.destroy()    
    btn_v.destroy()
    btn_s.destroy()
    btn_t.destroy()
    
    lbl_s.grid(column=0, row=0)
    txt_s.grid(column=1,row=0)
    lbl_t.grid(column=0, row=1)
    txt_t.grid(column=1,row=1)
    btn_trigger.grid(column=1, row = 4)
def clicked_distance():
    lbl.destroy()
    btn_v.destroy()
    btn_s.destroy()
    btn_t.destroy()

    lbl_v.grid(column=0, row=0)
    txt_v.grid(column=1,row=0)
    lbl_t.grid(column=0, row=1)
    txt_t.grid(column=1,row=1)
    btn_trigger.grid(column=1, row = 4)
def clicked_time():
    lbl.destroy()
    btn_v.destroy()
    btn_s.destroy()
    btn_t.destroy()
    
    lbl_s.grid(column=0, row=0)
    txt_s.grid(column=1,row=0)
    lbl_v.grid(column=0, row=1)
    txt_v.grid(column=1,row=1)
    btn_trigger.grid(column=1, row = 4)
def clicked_push():
    v = txt_v.get
    s = txt_s.get
    t = txt_t.get
    text = 'velocity is' + v
    show = Label(window, text=text)
    show.grid(column=3, row = 3)
    
    
#def clicked_distance():
    
#def clicked_time():

window = Tk()
window.geometry('300x200')
window.title('Physics app')
#label:
lbl = Label(window, text='Hi,choose the unknown')
lbl.grid(column=0, row=0)


#velocity:
lbl_v = Label(window, text='type the velocity: ')
txt_v = Entry(window, width = 10)

btn_v = Button(window, text='Velocity', command=clicked_velocity)
btn_v.grid(column=2, row=1)

#distance:
lbl_s = Label(window, text='type the distance: ')
txt_s = Entry(window, width = 10)

btn_s = Button(window, text='Distance', command=clicked_distance)
btn_s.grid(column=2, row=2)

#time:
lbl_t = Label(window, text='type time: ')
txt_t = Entry(window, width = 10)

btn_t = Button(window, text='Time', command=clicked_time)
btn_t.grid(column=2, row=3)

#trigger button
btn_trigger = Button(window, text='Press to trigger', command=clicked_push)

window.mainloop()


sleep(5)


