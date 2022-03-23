#Original code from http://y-okamoto-psy1949.la.coocan.jp/Python/en1/DigitalClock/
import tkinter as tk
from tkinter import *
from time import strftime

#Creates an instance of the Tk class, which initializes Tk and creates its associated Tcl interpreter. It also creates a toplevel window, known as the root window, which serves as the main window of the application.
root = tk.Tk()
#Label for the top of the window
root.title("Futurama: Always Watching!") 

#Creates Frame for Text
frame = tk.Frame(root)

# #Creates the Close button, OPTIONAL
#def f_close(event):
#   root.destroy()
# button = tk.Button(frame, text = 'Close')
# button.grid(row = 0, column = 10, padx = 5, sticky = 'e')
# button.bind('<Button-1>', f_close)

# Adds image file
bgImage = PhotoImage(file = "futurama_audience_500x287.png") #must be .png

# Creates Canvas for Picture
daCanvas = Canvas(frame, width = 500, height = 283) #Set Canvas width and height based on pic dimensions
daCanvas.grid(row = 1, columnspan = 11, rowspan = 1)
#Creates Picture
daCanvas.create_image( 0, 0, image = bgImage, anchor = "nw")

#Sets Frame up for Text, This geometry manager organizes widgets in blocks before placing them in the parent widget.
frame.pack()
#.create_text(x,y, options...); justify= LEFT, RIGHT, or CENTER; fill='Text's Color', tags='mytext' is what will be used to call this later
daCanvas.create_text(150, 150, justify=LEFT,text = ' ', fill='#000000',  font = ('ds-digital', 50), tags = 'mytext') #OPTIONAL after the font size (50 in this instance) add a comma ( , ) and 'bold' for boldface or 'italic' for italic

#Creates a function for displaying and checking the time
def check_time():
    daDate = strftime('%b %d %g') #Displays Month Day Year
    daLine="\n" #new line
    daTime =strftime('%T') #Displays time on the new ss line as HH:MM:SS in 24 hour format
    daCanvas.itemconfig('mytext', text = daDate+daLine+daTime) #'mytext' calls text parameters from create_text, text= combines the 3 objects together
    root.after(100, check_time) #Continual Refresh

#Calls function check_time to run it 
check_time()
#Continually loops the program so it keeps running until you close the window
root.mainloop()
