from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

##HardWare
led = LED(18)

##GUI
win = Tk() ##Create a Window
win.title("Morse Code Generator")
myFont = tkinter.font.Font(family = 'Arial', size = 16, weight = "bold")

## EVENT MORSECODE REPRESENTATION FOR EVERY LETTER
def MorseCodeGenerator(userInput):
    for letter in userInput:
        if (letter.lower() == 'a'):
            MorseCode_Dot()
            MorseCode_Dash()
        
        elif (letter.lower() == 'b'):
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dot()
            MorseCode_Dot()
        
        elif (letter.lower() == 'c'):
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dash()
            MorseCode_Dot()
        
        elif (letter.lower() == 'd'):
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dot()
        
        elif (letter.lower() == 'e'):
            MorseCode_Dot()
        
        elif (letter.lower() == 'f'):
            MorseCode_Dot()
            MorseCode_Dot()
            MorseCode_Dash()
            MorseCode_Dot()
        
        elif (letter.lower() == 'g'):
            MorseCode_Dash()
            MorseCode_Dash()
            MorseCode_Dot()
        
        elif (letter.lower() == 'h'):
            MorseCode_Dot()
            MorseCode_Dot()
            MorseCode_Dot()
            MorseCode_Dot()
        
        elif (letter.lower() == 'i'):
            MorseCode_Dot()
            MorseCode_Dot()
        
        elif (letter.lower() == 'j'):
            MorseCode_Dot()
            MorseCode_Dash()
            MorseCode_Dash()
            MorseCode_Dash()
        
        elif (letter.lower() == 'k'):
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dash()
        
        elif (letter.lower() == 'l'):
            MorseCode_Dot()
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dot()
        
        elif (letter.lower() == 'm'):
            MorseCode_Dash()
            MorseCode_Dash()
        
        elif (letter.lower() == 'n'):
            MorseCode_Dash()
            MorseCode_Dot()
        
        elif (letter.lower() == 'o'):
            MorseCode_Dash()
            MorseCode_Dash()
            MorseCode_Dash()
        
        elif (letter.lower() == 'p'):
            MorseCode_Dot()
            MorseCode_Dash()
            MorseCode_Dash()
            MorseCode_Dot()
        
        elif (letter.lower() == 'q'):
            MorseCode_Dash()
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dash()
        
        elif (letter.lower() == 'r'):
            MorseCode_Dot()
            MorseCode_Dash()
            MorseCode_Dot()
        
        elif (letter.lower() == 't'):
            MorseCode_Dash()
        
        elif (letter.lower() == 'u'):
            MorseCode_Dot()
            MorseCode_Dot()
            MorseCode_Dash()
        
        elif (letter.lower() == 'v'):
            MorseCode_Dot()
            MorseCode_Dot()
            MorseCode_Dot()
            MorseCode_Dash()
        
        elif (letter.lower() == 'w'):
            MorseCode_Dot()
            MorseCode_Dash()
            MorseCode_Dash()
        
        elif (letter.lower() == 'x'):
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dot()
            MorseCode_Dash()
        
        elif (letter.lower() == 'y'):
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dash()
            MorseCode_Dash()
        
        elif (letter.lower() == 'z'):
            MorseCode_Dash()
            MorseCode_Dash()
            MorseCode_Dot()
            MorseCode_Dot()
            

## This method turns led on for 1 second
def MorseCode_Dot():
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)


## This method turns led on for 3 seconds
def MorseCode_Dash():
    led.on()
    time.sleep(3)
    led.off()
    time.sleep(1)
    
def UserEnter():
    userInput = Text_Box.get("1.0","end-1c")
    MorseCodeGenerator(userInput)
        
## CREATE WIDGETS
Text_Box = Text(win, height = 3, width = 20, bg = "white")
Text_Box.grid(row=0,column=1, padx = 20, pady = 20)

Enter = Button(win, text = 'ENTER', font = myFont, command = UserEnter, bg = 'grey', height = 1, width = 30) ## CREATE RED LED WIDGET
Enter.grid(row=1,column=1)
    
win.mainloop();