from cgitb import text
import tkinter as tk
import random as rng

root = tk.Tk()

#window setting 
root.geometry("300x300")

root.columnconfigure(0,weight=1)
root.rowconfigure(1,weight=1)


#top bar
topFrame = tk.Frame(root)

#--min
tk.Label(topFrame,text='min').pack(side=tk.LEFT)
minEntry = tk.Entry(topFrame,width=10)
minEntry.insert(tk.END,"0")
minEntry.pack(side=tk.LEFT,expand=0)

#--max
maxEntry = tk.Entry(topFrame,width=10)
maxEntry.insert(tk.END,"10")
maxEntry.pack(side=tk.RIGHT,expand=0)
tk.Label(topFrame,text="max").pack(side=tk.RIGHT)

#topFrame.pack(side=tk.TOP,fill=tk.X)
topFrame.grid(row=0,column=0,sticky=tk.W + tk.E)

#center label
valueLabel = tk.Label(root,text='00',background='pink',font=('FreeMono',50))
#valueLabel.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
valueLabel.grid(row=1,column=0,sticky=tk.N + tk.S + tk.E + tk.W)

#buttom button
def generate_number(min,max):
    try:
        min = int(min)
        max = int(max)

        randValue = rng.randint(min,max)
        if randValue < 0 and randValue > -10:
            finalstring = str(randValue)
            finalstring = finalstring[len(finalstring)-1]
            valueLabel.configure(text="-0" + finalstring)
        elif randValue < 10 and randValue >= 0:
            valueLabel.configure(text="0"+str(randValue))
        else:
            valueLabel.configure(text=str(randValue))
    except Exception as e:
        print("error:" + str(e))


sendButton = tk.Button(root,text='start',height=4,command=lambda: generate_number(minEntry.get(),maxEntry.get()))
#sendButton.pack(side=tk.TOP,fill=tk.X,expand=1)
sendButton.grid(row=2,column=0,sticky=tk.S + tk.W + tk.E)

root.mainloop()