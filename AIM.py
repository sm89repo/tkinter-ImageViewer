from tkinter import *
from PIL import ImageTk,Image
    
root = Tk()
root.title('Image Viewer')
# root.iconbitmap('c')

myimg1=ImageTk.PhotoImage(Image.open(r"C:\Users\Madhwanath\Desktop\download.jpeg"))
myimg2=ImageTk.PhotoImage(Image.open(r"C:\Users\Madhwanath\Desktop\download (1).jpeg"))
myimg3=ImageTk.PhotoImage(Image.open(r"C:\Users\Madhwanath\Desktop\download (2).jpeg"))
myimg4=ImageTk.PhotoImage(Image.open(r"C:\Users\Madhwanath\Desktop\download.png"))
myimg5=ImageTk.PhotoImage(Image.open(r"C:\Users\Madhwanath\Desktop\download (3).jpeg"))

imglist=[myimg1,myimg2,myimg3,myimg4,myimg5]

my_label= Label(image=myimg1)
my_label.grid(row=0,column=0,columnspan=3)

current_image = 1

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global current_image

    my_label.grid_forget()
    my_label = Label(image=imglist[image_number-1])
    # button_forward = Button(root,text='>>',command=lambda:forward(image_number+1))
    # button_back = Button(root,text='<<',command=lambda:back(image_number-1))

    if image_number == 5:
        button_forward = Button(root,text='>>',state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    # button_back.grid(row=1,column=0)
    # button_forward.grid(row=1,column=2)

    current_image = image_number
    schedule_next_image()

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=imglist[image_number - 1])
    # button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    # button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root,text='<<',state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    # button_back.grid(row=1, column=0)
    # button_forward.grid(row=1, column=2)

    current_image = image_number
    schedule_next_image()


def schedule_next_image():
    global current_image
    next_image = current_image+1
    if next_image > len(imglist):
        next_image=1
    root.after(3000,lambda: forward(next_image))


# button_back = Button(root, text='<<',command=back,state=DISABLED)
button_exit = Button(root, text='Exit Program', command=root.quit)
# button_forward = Button(root, text='>>',command=lambda: forward(2))


# button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
# button_forward.grid(row=1,column=2)

schedule_next_image()

root.mainloop()






