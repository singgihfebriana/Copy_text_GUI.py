from tkinter import*
from time import*
import sys

class _chat_box:
    def __init__(self,master):
        self.master=master
        master.title("Chatbox")
        master.geometry("400x400+900+200")

        #Make label
        self.title1=Label(master,text="Silahkan tulis pesan anda dibawah ini :")
        self.title1.place(x=10,y=10)

        #make entry
        self.entry=Text(master,width=30,heigh=7)
        self.entry.place(x=10,y=29)

        #make button
        self.button=Button(master,text="Process your text",command=self.copy_text)
        self.button.place(x=10,y=160)

        self.button_exit=Button(master,text="Exit",width=5,command=self.exit)
        self.button_exit.place(x=187,y=160)

        #new_Frame
        self.frame_inside=LabelFrame(root,text="your output message :",width=100,heigh=100)
        self.frame_inside.place(x=10,y=200,width=300,heigh=170)
        self.label_output=Label(self.frame_inside)
        self.label_output.pack()
        self.label_countdown=Label(master,text="0",font=("arial",32))
        self.label_countdown.place(x=320,y=60)



    def copy_text(self):
        i=0
        while i<=10:
            self.label_countdown["text"]=[i]
            i+=1
            root.update()
            sleep(1)
            if i==10:
                self.label_output.config(text=self.entry.get(1.0,END+"-1c"),font=12)

    def exit(self):
        sys.exit()

root=Tk()
chatbox=_chat_box(root)
root.mainloop()
