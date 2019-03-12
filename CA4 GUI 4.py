from tkinter import *
import math
import statistics
import random
from PIL import ImageTk,Image
import time
import math
import sys
import os

# give the insatnce of Tk a name
window = Tk()

# Add a title to the window
window.title("Top Trumps Game")

#Add a background colour
window.configure( background='Red')

#background_image=PhotoImage(file="top.png")
#background_label = Label(window, image=background_image)
#background_label.place(x=200, y=0)

#sets size of window and where on x and y axis window will pop up 
window.geometry("1000x500")
window.resizable(0,0)
window.pack_propagate(0)



cards = []

class attributes() :
    def __init__(self, name, PhysicalStrength, FearFactor, KillingPower, HorrorRating, image):
        self.name = name
        self.PhysicalStrength = PhysicalStrength
        self.FearFactor = FearFactor
        self.KillingPower = KillingPower
        self.HorrorRating = HorrorRating
        self.image = Image.open(image)

        cards.append(self)

Werewolf=attributes('Werewolf',88,78,85,76,"Monsters//werewolf.png")
KingKong=attributes('King Kong',100,90,97,70,"Monsters//king kong.png")
PhantomoftheOpera=attributes('Phantom of the Opera',77,67,74,87,"Monsters//phantom.png")
Godzilla=attributes("Godzilla",98,88,95,77,"Monsters//godzilla.png")
HeadHunter=attributes('HeadHunter',88,78,85,91,"Monsters//headhunter.png")
TheThing=attributes('The Thing',91,81,88,65,"Monsters//thing.png")
TheFreak=attributes('The Freak',94,54,91,96,"Monsters//freak.png")
Dracula=attributes('Dracula',91,81,86,100,"Monsters//dracula.png")
Skelton=attributes('Skelton',65,55,62,90,"Monsters//skelton.png")
ApeMan=attributes('Ape Man',81,71,76,69,"Monsters//ape.png")
VampireBat=attributes('Vampire Bat',45,80,60,84,"Monsters//vampire.png")
GraniteMan=attributes('Granite Man',92,82,89,71,"Monsters//granite.png")

#/////////////////////////////////////////////////////////////////////////////////
def shuffle():
    random.shuffle(cards)

button_shuffle = Button(window, text="Please click here to shuffle cards",bg='blue',fg='black',width=25, command=shuffle)
button_shuffle.place(bordermode=OUTSIDE, height=30, width=220,x=540,y=210)

#/////////////////////////////////////////////////////////////////////////////////

def deal():
    
    human = []
    computer = []

    if len(cards) > 0:
        human.append(cards.pop(0))
        computer.append(cards.pop(0))


    humanCard = human.pop(0)
    computersCard = computer.pop(0)

    #img = Image.open(playersCard.image)
    #img.show()
    
    humancardshow = ImageTk.PhotoImage(humanCard.image)
    panel = Label(image = humancardshow)
    panel.configure(image = humancardshow)
    panel.place(x=300,y=50)
    panel.image = humancardshow

    #text1=tk.Text(window,height=10,width=10)
    #text1.config(state="your card is:" , humancard.name)

    print("your card Name:", humanCard.name)
    print("a. your PhysicalStrength:", humanCard.PhysicalStrength)
    print("b. your FearFactor:", humanCard.FearFactor)
    print("c. your KillingPower:", humanCard.KillingPower)
    print("d. your HorrorRating:", humanCard.HorrorRating)

    

    
    
button_start = Button(window, text=" click to start game ",bg='cyan',fg='black',activebackground='blue',width=25, command=deal)
button_start.place(bordermode=OUTSIDE, height=30, width=200,x=550,y=150)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////BUTTTON COMMANDS///////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def comparePhysicalStrength():

    human = []
    computer = []

    if len(cards) > 0:
        human.append(cards.pop(0))
        computer.append(cards.pop(0))

    humanCard = human.pop(0)
    computersCard = computer.pop(0)

    print("computers Physical Strength:", computersCard.PhysicalStrength)
    Draw = (humanCard.PhysicalStrength == computersCard.PhysicalStrength)
    Win = (humanCard.PhysicalStrength > computersCard.PhysicalStrength)
#--------------------
    computercardshow = ImageTk.PhotoImage(computersCard.image)
    Comp = Label(image = computercardshow)
    Comp.configure(image = computercardshow)
    Comp.place(x=800,y=50)
    Comp.image = computercardshow
    print(computersCard.name)

    if  Draw:
        print("It's a tie!")
        human.append(humanCard)
        computer.append(computersCard)
    elif Win:
        print("You win this hand!")
        cards.append(humanCard)
        cards.append(computersCard)
        playerTurn = True
    else:
        print("You lose this hand!")
        computer.append(computersCard)
        computer.append(humanCard)
        playerTurn = False
#/////////////////////////////////////////////////////////////////////////////////

def compareFearFactor():

    human = []
    computer = []

    if len(cards) > 0:
        human.append(cards.pop(0))
        computer.append(cards.pop(0))

    humanCard = human.pop(0)
    computersCard = computer.pop(0)

    print("computers Fear Factor:", computersCard.FearFactor)
    Draw = (humanCard.FearFactor == computersCard.FearFactor)
    Win = (humanCard.FearFactor > computersCard.FearFactor)
#--------------------
    computercardshow = ImageTk.PhotoImage(computersCard.image)
    Comp = Label(image = computercardshow)
    Comp.configure(image = computercardshow)
    Comp.place(x=800,y=50)
    Comp.image = computercardshow

    DisplayResultFear.configure( text = " computers FearFactor: " + str(computersCardFearFactor))

    if  Draw:
        print("It's a tie!")
        human.append(humanCard)
        computer.append(computersCard)
    elif Win:
        print("You win this hand!")
        cards.append(humanCard)
        cards.append(computersCard)
        playerTurn = True
    else:
        print("You lose this hand!")
        computer.append(computersCard)
        computer.append(humanCard)
        playerTurn = False

#/////////////////////////////////////////////////////////////////////////////////

def compareKillingPower():

    human = []
    computer = []

    if len(cards) > 0:
        human.append(cards.pop(0))
        computer.append(cards.pop(0))

    humanCard = human.pop(0)
    computersCard = computer.pop(0)

    print("computers Killing Power:", computersCard.KillingPower)
    Draw = (humanCard.KillingPower == computersCard.KillingPower)
    Win = (humanCard.KillingPower> computersCard.KillingPower)
#--------------------
    computercardshow = ImageTk.PhotoImage(computersCard.image)
    Comp = Label(image = computercardshow)
    Comp.configure(image = computercardshow)
    Comp.place(x=800,y=50)
    Comp.image = computercardshow

    if  Draw:
        print("It's a tie!")
        human.append(humanCard)
        computer.append(computersCard)
    elif Win:
        print("You win this hand!")
        cards.append(humanCard)
        cards.append(computersCard)
        playerTurn = True
    else:
        print("You lose this hand!")
        computer.append(computersCard)
        computer.append(humanCard)
        playerTurn = False

#/////////////////////////////////////////////////////////////////////////////////

def compareHorrorRating():

    human = []
    computer = []

    if len(cards) > 0:
        human.append(cards.pop(0))
        computer.append(cards.pop(0))

    humanCard = human.pop(0)
    computersCard = computer.pop(0)

    print("computers Horror Rating:", computersCard.HorrorRating)
    Draw = (humanCard.HorrorRating == computersCard.HorrorRating)
    Win = (humanCard.HorrorRating> computersCard.HorrorRating)
#--------------------
    computercardshow = ImageTk.PhotoImage(computersCard.image)
    Comp = Label(image = computercardshow)
    Comp.configure(image = computercardshow)
    Comp.place(x=800,y=50)
    Comp.image = computercardshow

    if  Draw:
        print("It's a tie!")
        human.append(humanCard)
        computer.append(computersCard)
    elif Win:
        print("You win this hand!")
        cards.append(humanCard)
        cards.append(computersCard)
        playerTurn = True
    else:
        print("You lose this hand!")
        computer.append(computersCard)
        computer.append(humanCard)
        playerTurn = False

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#button_reset=Button (window,text=' Press to reset Game    ',command=restart,borderwidth=.1)
#button_reset.place(bordermode=OUTSIDE, height=30, width=200,x=550,y=280)

    
#creates button to select answers
button_Physical=Button(window,width=14,text=' Physical Strength    ',command=comparePhysicalStrength,)
button_Fear=Button(window,width=14,text='   Fear Factor    ', command=compareFearFactor,borderwidth=.1)
button_Killing=Button(window,width=14,text='   Killing Power    ', command= compareKillingPower,borderwidth=.1)
button_Horror=Button(window,width=14,text='   Horror Rating    ', command= compareHorrorRating,borderwidth=.1)

#sets the button in set postion 
button_Physical.place(bordermode=OUTSIDE, height=30, width=200,x=30,y=100)
button_Fear.place(bordermode=OUTSIDE, height=30, width=200,x=30,y=200)
button_Killing.place(bordermode=OUTSIDE, height=30, width=200,x=30,y=300)
button_Horror.place(bordermode=OUTSIDE, height=30, width=200,x=30,y=400)

label_TEXT= Label (window,text="v Choose an Attribute v", relief="raised")
label_TEXT.place(bordermode=OUTSIDE, height=60, width=200,x=30,y=30)
label_TEXT.configure(bg='yellow',bd=15)


window.mainloop()

