import tkinter
from tkinter import *
import math
import random
from threading import Thread 
from collections import defaultdict
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import time
import random

global mobile
global labels
global mobile_x
global mobile_y
global text
global canvas
global mobile_list
global filename
global p1,p2,p3
global line1,line2,line3
option = 0
global root
optimization = []
non_optimize = []
def optimizeDistance(iot_x,iot_y,x1,y1):
    flag = False
    for i in range(len(iot_x)):
        dist = math.sqrt((iot_x[i] - x1)**2 + (iot_y[i] - y1)**2)
        if dist < 80:
            flag = True
            break
    return flag

    
def startDataTransferSimulation(received_value,text,canvas,line1,line2,line3,x1,y1,x2,y2,x3,y3):
    class SimulationThread(Thread):
        def __init__(self,received_value,text,canvas,line1,line2,line3,x1,y1,x2,y2,x3,y3): 
            Thread.__init__(self) 
            self.canvas = canvas
            self.line1 = line1
            self.line2 = line2
            self.line3 = line3
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.x3 = x3
            self.y3 = y3
            self.text = text
            self.received_value = received_value
 
        def run(self):
            time.sleep(1)
            for i in range(0,3):
                self.canvas.delete(self.line1)
                self.canvas.delete(self.line2)
                self.canvas.delete(self.line3)
                time.sleep(1)
                self.line1 = canvas.create_line(self.x1, self.y1,self.x2, self.y2,fill='black',width=3)
                self.line2 = canvas.create_line(self.x2, self.y2,self.x3, self.y3,fill='black',width=3)
                self.line3 = canvas.create_line(self.x3, self.y3,25, 370,fill='black',width=3)
                time.sleep(1)
            self.text.insert(END,"\nServer Received Network Sense value: "+str(received_value)+"\n")    
            self.canvas.delete(self.line1)
            self.canvas.delete(self.line2)
            self.canvas.delete(self.line3)
            canvas.update()
                
    newthread = SimulationThread(received_value,text,canvas,line1,line2,line3,x1,y1,x2,y2,x3,y3) 
    newthread.start()
    
    
def networkSystem():
    global mobile
    global labels
    global mobile_x
    global mobile_y
    mobile = []
    mobile_x = []
    mobile_y = []
    labels = []
    canvas.update()
    x = 5
    y = 350
    mobile_x.append(x)
    mobile_y.append(y)
    name = canvas.create_oval(x,y,x+40,y+40, fill="blue")
    lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 7 italic bold",text="BS")
    labels.append(lbl)
    mobile.append(name)

    for i in range(1,20):
        run = True
        while run == True:
            x = random.randint(100, 450)
            y = random.randint(50, 600)
            flag = optimizeDistance(mobile_x,mobile_y,x,y)
            if flag == False:
                mobile_x.append(x)
                mobile_y.append(y)
                run = False
                name = canvas.create_oval(x,y,x+40,y+40, fill="red")
                lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 8 italic bold",text="Node "+str(i))
                labels.append(lbl)
                mobile.append(name)
    

def initializeNetwork():
    text.delete('1.0', END)
    global p1,p2,p3
    distance = 10000
    global leaf1, leaf2, leaf3
    leaf1 = 0
    leaf2 = 0
    leaf3 = 0
    for i in range(1,20):
        x1 = mobile_x[i]
        y1 = mobile_y[i]
        dist = math.sqrt((x1 - 5)**2 + (y1 - 350)**2)
        if dist < distance and y1 > 5 and y1 < 200:
            distance = dist
            leaf1 += 1
            p1 = i
    print(distance)        
    distance = 10000
    for i in range(1,20):
        x1 = mobile_x[i]
        y1 = mobile_y[i]
        dist = math.sqrt((x1 - 5)**2 + (y1 - 350)**2)
        if dist < distance and i != p1 and y1 > 250 and y1 <= 350 :
            distance = dist
            leaf2 += 1
            p2 = i
    print(distance)
    distance = 10000
    for i in range(1,20):
        x1 = mobile_x[i]
        y1 = mobile_y[i]
        dist = math.sqrt((x1 - 5)**2 + (y1 - 350)**2)
        if dist < distance and i != p1 and i != p2 and y1 > 450 and y1 < 650:
            distance = dist
            p3 = i
            leaf3 += 1
    print(distance)
    print(str(leaf1)+" "+str(leaf2)+" "+str(leaf3))            
    text.insert(END,"Selected Actuator 1 is : "+str(p1)+"\n")
    text.insert(END,"Selected Actuator 2 is : "+str(p2)+"\n")
    text.insert(END,"Selected Actuator 3 is : "+str(p3)+"\n")
    canvas.delete(mobile[p1])
    canvas.delete(mobile[p2])
    canvas.delete(mobile[p3])
    canvas.delete(labels[p1])
    canvas.delete(labels[p2])
    canvas.delete(labels[p3])
    name = canvas.create_oval(mobile_x[p1],mobile_y[p1],mobile_x[p1]+40,mobile_y[p1]+40, fill="green")
    mobile[p1] = name
    name = canvas.create_oval(mobile_x[p2],mobile_y[p2],mobile_x[p2]+40,mobile_y[p2]+40, fill="green")
    mobile[p2] = name
    name = canvas.create_oval(mobile_x[p3],mobile_y[p3],mobile_x[p3]+40,mobile_y[p3]+40, fill="green")
    mobile[p3] = name
    lbl = canvas.create_text(mobile_x[p1]+20,mobile_y[p1]-10,fill="green",font="Times 10 italic bold",text="A1-"+str(p1))
    labels[p1] = lbl
    lbl = canvas.create_text(mobile_x[p2]+20,mobile_y[p2]-10,fill="green",font="Times 10 italic bold",text="A2-"+str(p2))
    labels[p2] = lbl
    lbl = canvas.create_text(mobile_x[p3]+20,mobile_y[p3]-10,fill="green",font="Times 10 italic bold",text="A3-"+str(p3))
    labels[p3] = lbl

    canvas.create_oval(50,5,500,245)
    canvas.create_oval(50,240,500,450)
    canvas.create_oval(50,430,500,670)
    
    canvas.update()

def optimizationGraph():
    global optimization, non_optimize
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Technique Name')
    plt.ylabel('Resources Consumption')
    plt.plot(optimization,"ro-", color = 'blue')
    plt.plot(non_optimize,"ro-", color = 'red')
    plt.legend(['Optimized', 'Non-Optimize'], loc='upper left')
    plt.title('Optimized Network System Graph')
    plt.show()

def close():
    root.destroy()

def optimizeNetwork():
    global option, optimization, non_optimize
    global line1,line2,line3
    text.delete('1.0', END)
    src = int(mobile_list.get())
    start_time = time.time()
    if option == 1:
        canvas.delete(line1)
        canvas.delete(line2)
        canvas.delete(line3)
        canvas.update()
    src_x = mobile_x[src]
    src_y = mobile_y[src]
    distance = 10000
    hop = 0
    gateway = 0
    for i in range(1,20):
        temp_x = mobile_x[i]
        temp_y = mobile_y[i]
        if i != src and i != p1 and i != p2 and i != p3 and temp_x < src_x:
            dist = math.sqrt((src_x - temp_x)**2 + (src_y - temp_y)**2)
            if dist < distance:
                distance = dist
                hop = i
    if hop != 0:
        hop_x = mobile_x[hop]
        hop_y = mobile_y[hop]
        distance1 = math.sqrt((hop_x - mobile_x[p1])**2 + (hop_y - mobile_y[p1])**2)
        distance2 = math.sqrt((hop_x - mobile_x[p2])**2 + (hop_y - mobile_y[p2])**2)
        distance3 = math.sqrt((hop_x - mobile_x[p3])**2 + (hop_y - mobile_y[p3])**2)
        if distance1 <= distance2 and distance1 <= distance3:
            gateway = p1
            optimization.append(distance1/100)
            non_optimize.append((distance1/100) * 2)
        elif distance2 <= distance1 and distance2 <= distance3:
            optimization.append(distance2/100)
            non_optimize.append((distance2/100) * 2)
            gateway = p2
        else:
            optimization.append(distance3/100)
            non_optimize.append((distance3/100) * 2)
            gateway = p3
    if gateway != 0 and hop != 0:
        value = str(random.randint(18,50))
        text.insert(END,"Selected Source Node is : "+str(src)+"\ngenerated sense value = "+value+"\n\n")
        text.insert(END,"Selected Neighbour Node is : "+str(hop)+"\n\n")
        text.insert(END,"Selected Actuator Node is : "+str(gateway)+"\n")
        line1 = canvas.create_line(mobile_x[src]+20, mobile_y[src]+20,mobile_x[hop]+20, mobile_y[hop]+20,fill='black',width=3)
        line2 = canvas.create_line(mobile_x[hop]+20, mobile_y[hop]+20,mobile_x[gateway]+20, mobile_y[gateway]+20,fill='black',width=3)
        line3 = canvas.create_line(mobile_x[gateway]+20, mobile_y[gateway]+20,mobile_x[0]+20, mobile_y[0]+20,fill='black',width=3)
        startDataTransferSimulation(int(value),text,canvas,line1,line2,line3,(mobile_x[src]+20),(mobile_y[src]+20),(mobile_x[hop]+20),(mobile_y[hop]+20),(mobile_x[gateway]+20),(mobile_y[gateway]+20))
        option = 1        
    else:
        text.insert(END,"No Optimize path node found. Try another source\n")
            

    
def Main():
    global root
    global tf1
    global text
    global canvas
    global mobile_list
    root = tkinter.Tk()
    root.geometry("1300x1200")
    root.title("Data-Based Receding Horizon Control of Linear Network Systems")
    root.resizable(True,True)
    font1 = ('times', 12, 'bold')

    canvas = Canvas(root, width = 800, height = 700)
    canvas.pack()

    l1 = Label(root, text='Node ID:')
    l1.config(font=font1)
    l1.place(x=820,y=10)

    mid = []
    for i in range(1,20):
        mid.append(str(i))
    mobile_list = ttk.Combobox(root,values=mid,postcommand=lambda: mobile_list.configure(values=mid))
    mobile_list.place(x=970,y=10)
    mobile_list.current(0)
    mobile_list.config(font=font1)

    createButton = Button(root, text="Network System Formation Phase", command=networkSystem)
    createButton.place(x=820,y=60)
    createButton.config(font=font1)

    initButton = Button(root, text="Initialize Network with Actuator Nodes", command=initializeNetwork)
    initButton.place(x=820,y=110)
    initButton.config(font=font1)

    algButton = Button(root, text="Optimize Network", command=optimizeNetwork)
    algButton.place(x=820,y=160)
    algButton.config(font=font1)

    graphButton = Button(root, text="Optimization Graph", command=optimizationGraph)
    graphButton.place(x=820,y=210)
    graphButton.config(font=font1)

    exitButton = Button(root, text="Exit", command=close)
    exitButton.place(x=820,y=260)
    exitButton.config(font=font1)

    text=Text(root,height=22,width=60)
    scroll=Scrollbar(text)
    text.configure(yscrollcommand=scroll.set)
    text.place(x=820,y=310)
    
    
    root.mainloop()
   
 
if __name__== '__main__' :
    Main ()
    
