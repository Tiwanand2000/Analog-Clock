from tkinter import*
from tkinter.font import BOLD
from PIL import Image,ImageTk,ImageDraw
from datetime import*
#  import time
from math import*
class Clock:
   def __init__(self,root):
      self.root = root
      self.root.title('Analog Clock') # Gives title
      self.root.geometry('1500x1500+10+0') # Gives dimensions
      self.root.config(bg='black') # background colour
   # add new text/label of relevant --------------bgcolor------------font-----------------------------textcolor-------dimensions

      title=Label(self.root,text='Analog Clock',background='black',font=('times new roman',50, BOLD),fg='Red').place(x=5,y=50,relwidth=1)
      
      self.lb1=Label(self.root,bg='cyan',bd=35,relief=GROOVE)
      self.lb1.place(x=515,y=200,height=500,width=500)
      #  self.clock_image()
      self.working()


   def clock_image(self,hr,mi,sec):
       clock=Image.new("RGB",(400,400),('Yellow'))
       draw=ImageDraw.Draw(clock) # Created new image png

       clc=Image.open('clock.png') 
       clc=clc.resize((300,300),Image.ANTIALIAS)
       clock.paste(clc,(50,50))

       draw.line((200,200,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=8) 
       draw.line((200,200,200+70*sin(radians(mi)),200-70*cos(radians(mi))),fill="black",width=4)
       draw.line((200,200,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="black",width=2)
       draw.ellipse((195,195,210,210),fill="black")

       clock.save("clock_image.jpg")
       
# Create how to make work the hands
   def working(self):
       h=datetime.now().time().hour
       m=datetime.now().time().minute
       s=datetime.now().time().second

       hr=(h/12)*360
       mi=(m/60)*360
       sec=(s/60)*360
       print(h,m,s)
      #  print(hr,mi,sec)
       self.clock_image(hr,mi,sec)
       self.img=ImageTk.PhotoImage(file="clock_image.jpg")
       self.lb1.config(image=self.img)
       self.lb1.after(200,self.working)
      

             
root = Tk()
obj = Clock(root)
root.mainloop()

 
