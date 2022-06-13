"""System Shutdown source code, schedule the shutdown or restart of your PC"""
"""@author Luca Porzio"""

from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import os
import sys

def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def works(evt):
	messagebox.showinfo("Image in the exe file", "This really works")

#Creating the window
window = Tk()
window.geometry('500x500')
window.minsize(500,500)
window.maxsize(500,500)
window.title('System Shutdown')

btn_state = False # The status of the nimated navigation bar
shutdown_scheduled = False # If shutdown or restart is already scheduled
nav_bar_in_movement = False # If the nav_bar is changing status

# setting the icon
window.iconbitmap(resource_path0(r'iconaS.ico'))

# initializing the lists for the widget, every widget will be deleted by category
labels = []
entrys = []
buttons = []

# the list "choice" contains the number of the current page, 0 is shutdown, 1 is restart and 2 is cancel
choice = []
# We always start from the shutdown page that is "1"
choice.append(1)

# This will load the images of the app, the functions allow to the final .exe file to open them
nav_icon = PhotoImage(file = resource_path0('navbar.png'))
close_icon = PhotoImage(file = resource_path0('close.png'))

# Creating the title label
labelTitolo = Label(
    window,
    text="System Shutdown",
    font = ('bold',30),
    width=20,
)

# Place the title label at this coordinates
labelTitolo.place(x = 15, y = 45)

# The main label, from this window the user will be able to choose when shutdown the PC
labelPar = Label(
    window,
    text = "Enter the time you want to pass\nbefore your PC is being shut down",
    font = ('bold',16),
    width=31
)
labelPar.place(x = 57, y = 103)

# Creating label for hours, minutes and seconds with respective input text fields
labelHo = Label(
    window,
    text = "Hours",
    font = ('bold',14),
    width = 10,
)
labelHo.place(x = 134, y = 170)

entryHo = Entry(window)
entrys.append(entryHo)

entryHo.place(x = 225, y = 175)

labelMin = Label(
    window,
    text = "Minutes",
    font = ('bold',14),
    width = 10,
)
labelMin.place(x = 127, y = 210)

entryMin = Entry(window)
entryMin.place(x = 225, y = 215)
entrys.append(entryMin)

labelSec = Label(
    window,
    text = "Seconds",
    font = ('bold',14),
    width = 10,
)
labelSec.place(x = 120, y = 250)

entrySec = Entry(window)
entrySec.place(x = 225, y = 255)
entrys.append(entrySec)

# This is the main function to shutdown the PC, if conditions are respected it will start the scheduled shutdown
def confirmShutdown():
    global nav_bar_in_movement
    # Get the input of hours, minutes and seconds
    seconds = entrySec.get()
    minutes = entryMin.get()
    hours = entryHo.get()
    # If the input contains int values it will be okay
    if not nav_bar_in_movement:
        try:
            # If values are 0 or positive
            if (seconds + minutes + hours)== '' or int(seconds + minutes + hours) >= 0:

                time = ''

                background = Label(
                window,
                width=30,
                height=20
                )

                background.place(x=58,y=200)
                labels.append(background)
                # If the text fields are empty or the value is 0 it will immediately shutdown or restart the PC
                if (seconds + minutes + hours)== '' or int(seconds+minutes+hours) == 0:
                    # If we are on the shutdown page
                    if choice[0] == 1:
                        text = "Are you sure you want to shut down\nyour PC now?"
                    # If we are on the restart page
                    else:
                        text = "Are you sure you want to restart\nyour PC now?"

                    confirm = Label(
                            window,
                            borderwidth = 1,
                            relief = "solid",
                            text = text, # Using the correct variable for the answer
                            background="white",  # Set the background color to black
                            font = ('bold',14),
                            width = 35,
                            height = 4
                        )

                # If the value isn't 0 we will calculate the time to shutdown or restart the PC
                else:
                    if hours != '':
                        if hours == '1':
                            time += str(hours +' hour')
                        else:
                            time += str(hours +' hours')
                    if minutes != '':
                        if hours !='':
                            time += ', '
                        if minutes == '1':
                            time += str(minutes + ' minute')
                        else:
                            time += str(minutes + ' minutes')
                    if seconds != '':
                        if hours !='' or minutes != '':
                            time += ' e '
                        if seconds == '1':
                            time += str(seconds +' second')
                        else:
                            time += str(seconds + ' seconds')

                    # Same procedure but now with the confirm window
                    if choice[0] == 1:
                        text = "Are you sure you want to shut down your PC\nbetween {}?".format(time)
                    else:
                        text = "Are you sure you want to restart your PC\nbetween {}?".format(time)

                    # Create the confirm window
                    confirm = Label(
                        window,
                        borderwidth = 1,
                        relief = "solid",
                        text = text,
                        background = "white",  # Set the background color to black
                        font = ('bold',14),
                        width = 35,
                        height = 4
                    )
                
                confirm.place(x = 55,y = 200)
                labels.append(confirm)

                # Destroy the confirm windows
                def delConf():
                    confirm.destroy()
                    bottoneNo.destroy()
                    bottoneSi.destroy()
                    background.destroy()

                # Creating the buttons of YES and NO for the confirm
                bottoneSi = tk.Button(
                    text="Yes",
                    width=8,
                    height=2,
                    font = ('bold',14),
                    bg="lightgreen",
                    fg="black",
                    command = lambda:[shutdown(), delConf()]
                )

                bottoneSi.place(x = 143, y = 300)

                # Append the button YES in the list of buttons
                buttons.append(bottoneSi)
                
                bottoneNo = tk.Button(
                    text="No",
                    width=8,
                    height=2,
                    font = ('bold',14),
                    bg="#fd453c",
                    fg="black",
                    command = delConf
                )

                bottoneNo.place(x = 254, y = 300)

                # Append the button NO in the list of buttons
                buttons.append(bottoneNo)

            # If the Values are negative or invalid
            else:
                #Creating the background
                sfondo1 = Label(
                window,
                width=30,
                height=10
                )

                sfondo1.place(x=120,y=210)
                labels.append(sfondo1)


                color1 = Label(
                    window,
                    width=40,
                    height=5,
                    background = 'red'
                )
                labels.append(color1)

                color1.place(x = 101, y = 213)
                
                # Creating the error label to warn the user that the parameters are invalid
                error = Label(
                    window,
                    text="Enter a valid time!",
                    borderwidth = 1,
                    relief="solid",
                    background="white",
                    font = ('bold',14),
                    width=25,
                    height=3
            )
                error.place(x=105,y=218)
                labels.append(error)

                # Destroy the error label after that the user allows
                def delErr():
                    conErr.destroy()
                    error.destroy()
                    sfondo1.destroy()
                    color1.destroy()

                # Creating the button OKAY after the error
                conErr = tk.Button(
                    text="Okay",
                    height = 2,
                    width=8,
                    font = ('bold',14),
                    bg="white",
                    fg="black",
                    command = delErr
                )
                conErr.place(x=193,y=300)
                buttons.append(conErr)

        # Same procedure of the previous error but in case of exception, literally a copy - paste
        except:
            background = Label(
                window,
                width=30,
                height=10
                )

            background.place(x=120,y=210)
            labels.append(background)

            color = Label(
                    window,
                    width=40,
                    height=5,
                    background = 'red'
                )

            color.place(x = 101, y = 213)
            labels.append(color)

            error = Label(
                window,
                text="Enter a valid time!",
                borderwidth = 1,
                relief="solid",
                background="white",
                font = ('bold',14),
                width=25,
                height=3
            )
            error.place(x=105,y=218)
            labels.append(error)

            def delErr():
                    conErr.destroy()
                    error.destroy()
                    background.destroy()
                    color.destroy()

            conErr = tk.Button(
                text="Okay",
                height = 2,
                width=8,
                font = ('bold',14),
                bg="white",
                fg="black",
                command = delErr
                )
            conErr.place(x=193,y=300)
            buttons.append(conErr)

# Function that actually shutdown or restart the system
def shutdown():
    # We convert hours, minutes and seconds in to INT values after getting them from the text fields
    # The Exception could occur in case that the field is empty
    seconds = 0
    try:
        seconds = int(entrySec.get())
    except: None
    try:
        minutes = int(entryMin.get())
    except: None
    try:
        hours = int(entryHo.get())
    except: None

    # We use a line-command to schedule the shutdown, to use this we convert Hours and minutes in seconds adding them to the actual seconds var
    try:
        if int(hours) > 0:
            seconds += int(hours*60*60)
    except: None
    try:
        if int(minutes) > 0:
            seconds += int(minutes*60)
    except: None
    
    global shutdown_scheduled
    if int(seconds) >= 0:
        if not shutdown_scheduled:
            shutdown_scheduled = True
            
            try:
                os.system("shutdown /a")
            except: None

            sfondo3 = Label(
            window,
            width=25,
            height=10
            )

            sfondo3.place(x=120,y=240)
            labels.append(sfondo3)
            if choice[0] == 1:
                os.system("shutdown /s /f /t {}".format(seconds))
                spegni = Label(
                    window,
                    text="The PC will be turned off,\ndo you want to close the app?",
                    borderwidth = 1,
                    relief="solid",
                    background="white",
                    font = ('bold',14),
                    width=25,
                    height=3
                )

                spegni.place(x=105,y=218)
                labels.append(spegni)
            else:
                os.system("shutdown /r /f /t {}".format(seconds))
                spegni = Label(
                    window,
                    text="The PC will be restarted,\ndo you want to close the app?",
                    borderwidth = 1,
                    relief="solid",
                    background="white",
                    font = ('bold',14),
                    width=25,
                    height=3
                )

                spegni.place(x=105,y=218)
                labels.append(spegni)

            def delShutdown():
                spegni.destroy()
                yes.destroy()
                no.destroy()
                sfondo3.destroy()
            
            yes = tk.Button(
                text="Yes",
                width=10,
                font = ('bold',14),
                bg="lightgreen",
                fg="black",
                command = lambda:[delShutdown(),close()]
            )
            yes.place(x =120, y = 310)
            buttons.append(yes)

            no = tk.Button(
                text="No",
                width=10,
                font = ('bold',14),
                bg="#fd453c",
                fg="black",
                command = delShutdown
            )
            no.place(x =250, y = 310)
            buttons.append(no)

        else:
            background = Label(
                window,
                width=30,
                height=10
            )

            background.place(x=119,y=210)
            labels.append(background)

            color = Label(
                window,
                width=44,
                height=5,
                background = 'red'
            )

            color.place(x = 89, y = 213)
            labels.append(color)

            errorShutdown = Label(
            window,
            text="WARNING\nA system shutdown process is\n already in progress",
            borderwidth = 1,
            relief="solid",
            background="white",
            font = ('bold',14),
            width=27,
            height=3
            )

            errorShutdown.place(x=95,y=218)
            labels.append(errorShutdown)

            def delErrShutdown():
                conErrOk.destroy()
                errorShutdown.destroy()
                background.destroy()
                color.destroy()

            conErrOk = tk.Button(
            text="Okay",
            height = 2,
            width=8,
            font = ('bold',14),
            bg="white",
            fg="black",
            command = delErrShutdown
            )
            conErrOk.place(x=194,y=300)

            buttons.append(conErrOk)

button = tk.Button(
    text="Start",
    width=10,
    font = ('bold',14),
    bg="#bfe0f1",
    fg="black",
    command = lambda:[switchClose(),confirmShutdown()]
)
button.place(x =190, y = 310)

def switchClose():
    global btn_state
    global nav_bar_in_movement
    if btn_state is True and not nav_bar_in_movement:
        for button in buttons:
            try:
                button.destroy()
            except: None
        buttons.clear()
        
        for label in labels:
            try:
                label.destroy()
            except: None
        labels.clear()

        nav_bar_in_movement = True
        for x in range(251):
            NavBar.place(x = -x, y = 0)
            frame.update()

        nav_bar_in_movement = False
        frame.config(bg = 'black')

        btn_state = False

#------------ GRAPHIC PART -------------

def switch(): # Open and close the animated navigation bar
    global btn_state # get the actual status (Open or closed)
    global nav_bar_in_movement
    if btn_state is True:
        # Destrois all the elements in the screen
        for button in buttons:
            try:
                button.destroy()
            except: None
        buttons.clear()
        
        for label in labels:
            try:
                label.destroy()
            except: None
        labels.clear()

        nav_bar_in_movement = True
        for x in range(251): # This for shows the navigation bar with an animation
            NavBar.place(x = -x, y = 0)
            frame.update()

        nav_bar_in_movement = False
        frame.config(bg = 'black')

        btn_state = False # Change the status of the bar

    else:
        for button in buttons:
            try:
                button.destroy()
            except: None
        buttons.clear()
        
        for label in labels:
            try:
                label.destroy()
            except: None
        labels.clear()
        
        nav_bar_in_movement = True
        for x in range(-250, 0): # This for hides the navigation bar with an animation
            NavBar.place(x = x, y = 0)
            frame.update()

        nav_bar_in_movement = False
        frame.config(bg = 'SystemButtonFace')

        btn_state = True # Change the status of the bar

# Setting the navigation button and the frame with the nav bar
frame = Frame(window, bg = 'black')
frame.pack(side = 'top',fill = X)

navbar_btn = Button(frame, image = nav_icon, bg = 'black', bd = 0, command = switch)
navbar_btn.grid(row = 1, column = 1)

label = Label(window, font = 'ariel 18 bold')
label.place(x = 60, y = 250)

NavBar = Frame(window, bg = 'black', height = 1000, width = 250)
NavBar.place(x = -250, y = 0)

def chosen_option(msg): # Option choice
     switch()
     if msg == 1: # If the user choose "shutdown"
         if choice[0] != 1:

            choice[0] = 1

            labelTitolo.config(text = 'System Shutdown')

            labelPar.config(text = 'Enter the time you want to pass\nbefore your PC is being shut down')
         else:
             None

     elif msg == 2: # If the user choose "restart"
         if choice[0] != 2:

            choice[0] = 2

            labelTitolo.config(text = 'System Restart')

            labelPar.config(text = 'Enter the time you want to pass\nbefore your PC is being restarted')
         else:
             None
     else: # If the user choose "cancel"

         cancBackground = Label(
            window,
            width=30,
            height=20
            )

         cancBackground.place(x=58,y=200)
         labels.append(cancBackground)

         confirmCanc = Label( # Confirm label 
                window,
                borderwidth = 1,
                relief="solid",
                text="If you started a shutdown or restart process\nit will be canceled, continue?",
                #foreground="white",  # Set the text color to white
                background="white",  # Set the background color to black
                font = ('bold',14),
                width=35,
                height=4
            )

         confirmCanc.place(x=54,y=200)
         labels.append(confirmCanc)

         def delConfCanc(): # Delete all the elements to confirm the cancel statement
            confirmCanc.destroy()
            buttonNoCanc.destroy()
            buttonYesCanc.destroy()
            cancBackground.destroy()

         buttonYesCanc = tk.Button(
            text="Yes",
            width=8,
            height=2,
            font = ('bold',14),
            bg="lightgreen",
            fg="black",
            command = lambda:[cancelShutdown(), delConfCanc()]
            )

         buttonYesCanc.place(x = 143, y = 300)
         buttons.append(buttonYesCanc)
        
         buttonNoCanc = tk.Button(
            text="No",
            width=8,
            height=2,
            font = ('bold',14),
            bg="#fd453c",
            fg="black",
            command = delConfCanc
            )
         buttonNoCanc.place(x = 254, y = 300)

         buttons.append(buttonNoCanc)

def cancelShutdown(): # Cancel shutdown
    global shutdown_scheduled
    shutdown_scheduled = False

    os.system("shutdown /a")

    sfondo3 = Label(
        window,
        width=25,
        height=6
    )

    sfondo3.place(x=150,y=260)
    labels.append(sfondo3)

    confCanc = Label(
        window,
        text="Shutdown canceled",
        borderwidth = 1,
        relief="solid",
        background="white",
        font = ('bold',14),
        width=25,
        height=3
    )

    confCanc.place(x=105,y=218)
    labels.append(confCanc)
    
    def delConfCanc():
        confCanc.destroy()
        okCanc.destroy()
        sfondo3.destroy()
    
    okCanc = tk.Button(
        text = "Okay",
        width = 10,
        font = ('bold',14),
        bg = "white",
        fg = "black",
        command = delConfCanc
    )
    okCanc.place(x =180, y = 310)

    buttons.append(okCanc)
    
def close():
    sys.exit()

option1 = Button(NavBar, text = 'Shutdown', font = 'ariel 18 bold', bg = 'black', fg = 'white', activebackground = 'gray', activeforeground = 'white', bd = 0, command = lambda msg = 1:
chosen_option(msg)).place(x = 25, y = 60)

option2 = Button(NavBar, text = 'Restart', font = 'ariel 18 bold', bg = 'black', fg = 'white', activebackground = 'gray', activeforeground = 'white', bd = 0, command = lambda msg = 2:
chosen_option(msg)).place(x = 25, y = 120)

option2 = Button(NavBar, text = 'Cancel', font = 'ariel 18 bold', bg = 'black', fg = 'white', activebackground = 'gray', activeforeground = 'white', bd = 0, command = lambda msg = 3:
chosen_option(msg)).place(x = 25, y = 180)

close_btn = Button(NavBar, image = close_icon, bg = 'black', bd = 0, command = switch)
close_btn.place(x = 200, y = 5)

window.mainloop()
