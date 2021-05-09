##############################
# Author: TheNanoMachi       #
# Date Written: 2021/05/09   #
# Title: Russian Roulette    #
##############################

from tkinter import *
import random

root = Tk()
root.geometry("450x300")
root.title(" Russian Roulette ")

cyl = []

r = 0

rounds = 0


def Take_input():
    roundsSurvived = 0
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    for i in range (int(INPUT)):
        cyl.append(False)
        cyl[0] = True
    

def convertList(list):
    for i in range(len(list)):
        if list[i]:
            list[i] = "X"
        else:
            list[i] = "O"
    return list


def spincylinder(cylinder, cylinderArray):
    global rounds
    Output.delete("1.0", END)
    r = random.randint(0, cylinder-1)
    for i in range(len(cylinderArray)):
        cylinderArray[i] = False
    cylinderArray[r] = True
    print(convertList(cylinderArray))
    if r == 0:
        Output.insert(END, " You Died. You Survived "+str(rounds + 1)+" rounds.")
        print("You Died. You Survived "+str(rounds + 1)+" rounds.")
        rounds = 0
        raise SystemExit
        return True
    else:
        rounds += 1
        Output.insert(END, " You Survived")
        return False

img = PhotoImage(file = "rollthedice.png")

imglabel = Label(
    root,
    image = img
)

l = Label(text = "How many slots would you like? ")
inputtxt = Text(root, height = 1,
                width = 5,
                )

l1 = Label(text="\n")
Output = Text(root, height = 5, 
              width = 25, 
              )
  
Display = Button(root, height = 2,
                 width = 20, 
                 text = "Set",
                 relief = "groove",
                 command = lambda:Take_input())

l2 = Label(text="\n")

l3 = Label(text="\n")

l4 = Label(text="\n")

SpinButton = Button(root, height = 2,
                    width = 20,
                    text = "Spin",
                    relief = "groove",
                    command = lambda:spincylinder(len(cyl), cyl))

QuitButton = Button(root, height = 2,
                    width = 5,
                    text = "Quit",
                    relief = "groove",
                    command = lambda:quit())


l.configure(background = "brown")
l1.configure(background = "brown")
l2.configure(background = "brown")
l3.configure(background = "brown")
l4.configure(background = "brown")

imglabel.place(x=0,y=0)
l.pack()
inputtxt.pack()
l1.pack()
Display.pack()
l2.pack()
Output.pack()
l3.pack()
SpinButton.pack()
l4.pack()
QuitButton.pack()
mainloop()
