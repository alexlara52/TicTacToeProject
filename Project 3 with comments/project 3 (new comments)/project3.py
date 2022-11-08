from graphics import *
from time import sleep
import random
#
# Jacob Campbell, Alex Lara
# project3.py
# This program allows the user to play a game of tic-tac-toe
# with another user or with the computer. New Features include
# Keyboard features that allows player to enter out any name,
#  Random starter in one player mode with a 50% chance of AI
# Starting first,Zero player mode where you can watch two AI's duke it out,
# Custom difficulties where you can play against an easy or hard AI
# Custom Arcade mode that involves a suprise with mines - RNG


# makes window and associated variables
def window():
    # Creates the graphics window
    win = GraphWin("Keyboard", 300, 400)
     # Creates part of the grid
    a1 = Rectangle(Point(20, 70), Point(70, 120))
    a1.setFill("black")
    a1.setOutline("yellow")
    a1.draw(win)
    # Creates part of the grid
    b1 = Rectangle(Point(20, 120), Point(70, 170))
    b1.setFill("black")
    b1.setOutline("yellow")
    b1.draw(win)
    # Creates part of the grid
    c1 = Rectangle(Point(20, 170), Point(70, 220))
    c1.setFill("black")
    c1.setOutline("yellow")
    c1.draw(win)
    # Creates part of the grid
    d1 = Rectangle(Point(20, 220), Point(70, 270))
    d1.setFill("black")
    d1.setOutline("yellow")
    d1.draw(win)
    # Creates part of the grid
    e1 = Rectangle(Point(20, 270), Point(70, 320))
    e1.setFill("black")
    e1.setOutline("yellow")
    e1.draw(win)
       # Creates part of the grid
    a2 = Rectangle(Point(70, 70), Point(120, 120))
    a2.setFill("black")
    a2.setOutline("yellow")
    a2.draw(win)
    # Creates part of the grid
    b2 = Rectangle(Point(70, 120), Point(120, 170))
    b2.setFill("black")
    b2.setOutline("yellow")
    b2.draw(win)
    # Creates part of the grid
    c2 = Rectangle(Point(70, 170), Point(120, 220))
    c2.setFill("black")
    c2.setOutline("yellow")
    c2.draw(win)
    # Creates part of the grid
    d2 = Rectangle(Point(70, 220), Point(120, 270))
    d2.setFill("black")
    d2.setOutline("yellow")
    d2.draw(win)
    # Creates part of the grid
    e2 = Rectangle(Point(70, 270), Point(120, 320))
    e2.setFill("black")
    e2.setOutline("yellow")
    e2.draw(win)
       # Creates part of the grid
    a3 = Rectangle(Point(120, 70), Point(170, 120))
    a3.setFill("black")
    a3.setOutline("yellow")
    a3.draw(win)
    # Creates part of the grid
    b3 = Rectangle(Point(120, 120), Point(170, 170))
    b3.setFill("black")
    b3.setOutline("yellow")
    b3.draw(win)
    # Creates part of the grid
    c3 = Rectangle(Point(120, 170), Point(170, 220))
    c3.setFill("black")
    c3.setOutline("yellow")
    c3.draw(win)
    # Creates part of the grid
    d3 = Rectangle(Point(120, 220), Point(170, 270))
    d3.setFill("black")
    d3.setOutline("yellow")
    d3.draw(win)
    # Creates part of the grid
    e3 = Rectangle(Point(120, 270), Point(170, 320))
    e3.setFill("black")
    e3.setOutline("yellow")
    e3.draw(win)
       # Creates part of the grid
    a4 = Rectangle(Point(170, 70), Point(220, 120))
    a4.setFill("black")
    a4.setOutline("yellow")
    a4.draw(win)
    # Creates part of the grid
    b4 = Rectangle(Point(170, 120), Point(220, 170))
    b4.setFill("black")
    b4.setOutline("yellow")
    b4.draw(win)
    # Creates part of the grid
    c4 = Rectangle(Point(170, 170), Point(220, 220))
    c4.setFill("black")
    c4.setOutline("yellow")
    c4.draw(win)
    # Creates part of the grid
    d4 = Rectangle(Point(170, 220), Point(220, 270))
    d4.setFill("black")
    d4.setOutline("yellow")
    d4.draw(win)
    # Creates part of the grid
    e4 = Rectangle(Point(170, 270), Point(220, 320))
    e4.setFill("black")
    e4.setOutline("yellow")
    e4.draw(win)
       # Creates part of the grid
    a5 = Rectangle(Point(220, 70), Point(270, 120))
    a5.setFill("black")
    a5.setOutline("yellow")
    a5.draw(win)
    # Creates part of the grid
    b5 = Rectangle(Point(220, 120), Point(270, 170))
    b5.setFill("black")
    b5.setOutline("yellow")
    b5.draw(win)
    # Creates part of the grid
    c5 = Rectangle(Point(220, 170), Point(270, 220))
    c5.setFill("black")
    c5.setOutline("yellow")
    c5.draw(win)
    # Creates part of the grid
    d5 = Rectangle(Point(220, 220), Point(270, 270))
    d5.setFill("black")
    d5.setOutline("yellow")
    d5.draw(win)
    # Creates part of the grid
    e5 = Rectangle(Point(220, 270), Point(270, 320))
    e5.setFill("black")
    e5.setOutline("yellow")
    e5.draw(win)
    #Creates part of the grid
    e6 = Rectangle(Point(20, 320), Point(70, 370))
    e6.setFill("black")
    e6.setOutline("yellow")
    e6.draw(win)
    #Creates part of the grid
    BS = Rectangle(Point(70, 320), Point(170, 370))
    BS.setFill("black")
    BS.setOutline("yellow")
    BS.draw(win)
    #Creates part of the grid
    Enter = Rectangle(Point(170, 320), Point(270, 370))
    Enter.setFill("black")
    Enter.setOutline("yellow")
    Enter.draw(win)
    # draws the keys (This includes styles, sizes, faces, colors, points, etc)
    # A key
    akey = Text(Point(45, 100), "A")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # B key
    akey = Text(Point(95, 100), "B")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # C key
    akey = Text(Point(145, 100), "C")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # D key
    akey = Text(Point(195, 100), "D")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # E key
    akey = Text(Point(245, 100), "E")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # F Key
    akey = Text(Point(45, 150), "F")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # G Key
    akey = Text(Point(95, 150), "G")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # H Key
    akey = Text(Point(145, 150), "H")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # I key
    akey = Text(Point(195, 150), "I")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # J key
    akey = Text(Point(245, 150), "J")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # K key
    akey = Text(Point(45, 200), "K")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # L key
    akey = Text(Point(95, 200), "L")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # M key
    akey = Text(Point(145, 200), "M")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # N key
    akey = Text(Point(195, 200), "N")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # O key
    akey = Text(Point(245, 200), "O")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # P key
    akey = Text(Point(45, 250), "P")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # Q key
    akey = Text(Point(95, 250), "Q")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # R key
    akey = Text(Point(145, 250), "R")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # S key
    akey = Text(Point(195, 250), "S")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # T key
    akey = Text(Point(245, 250), "T")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # U key
    akey = Text(Point(45, 300), "U")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # V key
    akey = Text(Point(95, 300), "V")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # W key
    akey = Text(Point(145, 300), "W")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # X key
    akey = Text(Point(195, 300), "X")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # Y key
    akey = Text(Point(245, 300), "Y")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # Z key
    akey = Text(Point(45, 350), "Z")
    akey.setFace("courier")
    akey.setSize(23)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # Backspace Key
    akey = Text(Point(120, 345), "BackSpace")
    akey.setFace("courier")
    akey.setSize(12)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # Enter Key
    akey = Text(Point(220, 345), "Enter")
    akey.setFace("courier")
    akey.setSize(18)
    akey.setStyle("bold")
    akey.setTextColor("blue")
    akey.draw(win)
    # returns all objects (windows and keys)
    return win, a1, b1, c1, d1, e1, a2, b2, c2, d2, e2, a3, b3, c3, d3, e3, a4, b4, c4, d4, e4, a5, b5, c5, d5, e5, e6, BS, Enter, akey
# defines the checkpoint function accepts  2 args
def checkpoint(click, objects):
    # gets the point in the object whether it be rectangle or oval
    op1 = objects.getP1()
    op2 = objects.getP2()
    # returns conditional to see if click is inside object
    return op1.getX() < click.getX() and click.getX() < op2.getX() and op1.getY() < click.getY() and click.getY() < op2.getY()
# defines the Keyboard function accepts 2 args
def KeyBoard(Players,Control):
    # intializes variables
    win, a1, b1, c1, d1, e1, a2, b2, c2, d2, e2, a3, b3, c3, d3, e3, a4, b4, c4, d4, e4, a5, b5, c5, d5, e5, e6, BS, Enter, akey = window()
    # if its a one player game
    if Players == 1:
        # sets header for keyboard window
        Header = "Please enter player 1's name (limit 20 characters)"
        # initializes empty message string
        MSG = ''
        # intializes empty list for names
        PlayerNames = []
        # sets the text to display a typed playername in terms of size 
        Name1Text = Text(Point(150,50),MSG)
        Name1Text.setSize(14)
        Name1Text.draw(win)
        # sets the text for a second player if it is two player.
        Name2Text = Text(Point(150,20),Header)
        Name2Text.setSize(10)
        Name2Text.draw(win)
        # intializes variables for exits and enter key
        EnterButton = 0
        EXIT = 0
        LocalEXIT = 0
        # while loop to describe click control for keyboard
        while EnterButton == 0:
            # while loop to describe click control from a side window
            while LocalEXIT == 0:

                ClickControl = Control.checkMouse()
                # checks for clicks in the main menu
                if ClickControl != None:
                    # gets X of click
                    ClickControlX = ClickControl.getX()
                    # gets y of click
                    ClickControlY = ClickControl.getY()
                    # checks for a click in exit
                    if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                        EnterButton = 1
                        LocalEXIT = 1
                
                # gets a click from control panel
                
                click1 = win.checkMouse()
                # displays a message if none of the objects are clicked
                if click1 is None:
                    continue
                else:
                    # checks length to be 20
                    if len(MSG) >= 20:
                        # deletes last entry from string ## backspace
                        if checkpoint(click1, BS):
                            if MSG != '':
                                MSG = MSG[:-1]
                                Name1Text.setText(MSG)
                        # sets name 
                        elif checkpoint(click1, Enter):
                            EnterButton = 1
                            LocalEXIT = 2
                    # conditions for all the clicks and sets the msg string to whatever key was clicked as well as draws the Name
                    else:
                        # condtion for A key click
                        if checkpoint(click1, a1):
                            MSG += 'A'
                            Name1Text.setText(MSG)
                        # condtion for F key click
                        elif checkpoint(click1, b1):
                            MSG += 'F'
                            Name1Text.setText(MSG)
                        # condtion for K key click
                        elif checkpoint(click1, c1):
                            MSG += 'K'
                            Name1Text.setText(MSG)
                            # condtion for P key click
                        elif checkpoint(click1, d1):
                            MSG += 'P'
                            Name1Text.setText(MSG)
                            # condtion for U key click
                        elif checkpoint(click1, e1):
                            MSG += 'U'
                            Name1Text.setText(MSG)
                            # condtion for B key click
                        elif checkpoint(click1, a2):
                            MSG += 'B'
                            Name1Text.setText(MSG)
                            # condtion for G key click
                        elif checkpoint(click1, b2):
                            MSG += 'G'
                            Name1Text.setText(MSG)
                        # condtion for L key click
                        elif checkpoint(click1, c2):
                            MSG += 'L'
                            Name1Text.setText(MSG)
                            # condtion for Q key click
                        elif checkpoint(click1, d2):
                            MSG += 'Q'
                            Name1Text.setText(MSG)
                            # condtion for V key click
                        elif checkpoint(click1, e2):
                            MSG += 'V'
                            Name1Text.setText(MSG)
                            # condtion for C key click
                        elif checkpoint(click1, a3):
                            MSG += 'C'
                            Name1Text.setText(MSG)
                            # condtion for H key click
                        elif checkpoint(click1, b3):
                            MSG += 'H'
                            Name1Text.setText(MSG)
                            # condtion for M key click
                        elif checkpoint(click1, c3):
                            MSG += 'M'
                            Name1Text.setText(MSG)
                            # condtion for R key click
                        elif checkpoint(click1, d3):
                            MSG += 'R'
                            Name1Text.setText(MSG)
                            # condtion for W key click
                        elif checkpoint(click1, e3):
                            MSG += 'W'
                            Name1Text.setText(MSG)
                            # condtion for D key click
                        elif checkpoint(click1, a4):
                            MSG += 'D'
                            Name1Text.setText(MSG)
                            # condtion for I key click
                        elif checkpoint(click1, b4):
                            MSG += 'I'
                            Name1Text.setText(MSG)
                        # condtion for N key click
                        elif checkpoint(click1, c4):
                            MSG += 'N'
                            Name1Text.setText(MSG)
                        # condtion for S key click
                        elif checkpoint(click1, d4):
                            MSG += 'S'
                            Name1Text.setText(MSG)
                            # condtion for X key click
                        elif checkpoint(click1, e4):
                            MSG += 'X'
                            Name1Text.setText(MSG)
                            # condtion for E key click
                        elif checkpoint(click1, a5):
                            MSG += 'E'
                            Name1Text.setText(MSG)
                            # condtion for J key click
                        elif checkpoint(click1, b5):
                            MSG += 'J'
                            Name1Text.setText(MSG)
                            # condtion for O key click
                        elif checkpoint(click1, c5):
                            MSG += 'O'
                            Name1Text.setText(MSG)
                            # condtion for T key click
                        elif checkpoint(click1, d5):
                            MSG += 'T'
                            Name1Text.setText(MSG)
                        # condtion for Y key click
                        elif checkpoint(click1, e5):
                            MSG += 'Y'
                            Name1Text.setText(MSG)
                        # condtion for Z key click
                        elif checkpoint(click1, e6):
                            MSG += 'Z'
                            Name1Text.setText(MSG)
                        # condtion for backspace click
                        elif checkpoint(click1, BS):
                            if MSG != '':
                                MSG = MSG[:-1]
                                Name1Text.setText(MSG)
                        # condtion for enter key click
                        elif checkpoint(click1, Enter):
                            EnterButton = 1
                            LocalEXIT = 2
        # closes window
        win.close()
        # appends Playernames list with a name from the message string
        PlayerNames.append(MSG)
    # same thing as above just with 2 players.
    elif Players == 2:
        Header = "Please enter player 1's name (limit 20 characters)"
        MSG = ''
        PlayerNames = []
        Name1Text = Text(Point(150,50),MSG)
        Name1Text.setSize(14)
        Name1Text.draw(win)
        Name2Text = Text(Point(150,20),Header)
        Name2Text.setSize(10)
        Name2Text.draw(win)
        PlayerNames = []
        LocalEXIT = 0
        # iterates through to see if a local exit was clicked and also allows player 2 to select a name
        for i in range(0,2):
            if LocalEXIT != 0 and LocalEXIT != 2:
                break
            if i == 1:
                Header = "Please enter player 2's name (limit 20 characters)"
                Name2Text.setText(Header)
            MSG = ''
            Name1Text = Text(Point(150,50),MSG)
            Name1Text.setSize(14)
            Name1Text.draw(win)
            EnterButton = 0
            LocalEXIT = 0
            EXIT = 0
            # click control same as above 
            while EnterButton == 0:
                while LocalEXIT == 0:

                    ClickControl = Control.checkMouse()

                    if ClickControl != None:
                        ClickControlX = ClickControl.getX()
                        ClickControlY = ClickControl.getY()
                        if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                            EnterButton = 1
                            LocalEXIT = 1
                    # gets a click from control panel
                    click1 = win.checkMouse()
                    # displays a message if none of the objects are clicked
                    if click1 is None:
                        continue
                    else:
                        # again this is for player 2 see above more in depth comments but same code structure.
                        if len(MSG) >= 20:
                            if checkpoint(click1, BS):
                                if MSG != '':
                                    MSG = MSG[:-1]
                                    Name1Text.setText(MSG)
                            elif checkpoint(click1, Enter):
                                EnterButton = 1
                        else:
                            if checkpoint(click1, a1):
                                MSG += 'A'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, b1):
                                MSG += 'F'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, c1):
                                MSG += 'K'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, d1):
                                MSG += 'P'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, e1):
                                MSG += 'U'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, a2):
                                MSG += 'B'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, b2):
                                MSG += 'G'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, c2):
                                MSG += 'L'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, d2):
                                MSG += 'Q'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, e2):
                                MSG += 'V'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, a3):
                                MSG += 'C'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, b3):
                                MSG += 'H'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, c3):
                                MSG += 'M'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, d3):
                                MSG += 'R'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, e3):
                                MSG += 'W'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, a4):
                                MSG += 'D'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, b4):
                                MSG += 'I'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, c4):
                                MSG += 'N'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, d4):
                                MSG += 'S'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, e4):
                                MSG += 'X'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, a5):
                                MSG += 'E'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, b5):
                                MSG += 'J'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, c5):
                                MSG += 'O'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, d5):
                                MSG += 'T'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, e5):
                                MSG += 'Y'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, e6):
                                MSG += 'Z'
                                Name1Text.setText(MSG)
                            elif checkpoint(click1, BS):
                                if MSG != '':
                                    MSG = MSG[:-1]
                                    Name1Text.setText(MSG)
                            elif checkpoint(click1, Enter):
                                EnterButton = 1
                                LocalEXIT = 2
                    
            PlayerNames.append(MSG)
            Name1Text.undraw()
        # closes window for keyboard
        win.close()
    # if local exit is clicked
    if LocalEXIT == 1:
        EXIT = LocalEXIT
    return(PlayerNames,EXIT)

# defines control panel function no args
def controlPanel():
    # Creates all the control panel elements
    Control = GraphWin("Control",400,550)
    Control.setBackground(color_rgb(191,191,191))
    TicTacToe = Image(Point(200,57), "TicTacToe-Title.gif")
    TicTacToe.draw(Control)
    v2 = "v2.0"
    v2Text = Text(Point(200,117),v2)
    Board = Image(Point(200,262), "TicTacToe-Board.gif")
    Board.draw(Control)
    v2Text.draw(Control)
    sleep(3)
    Board.undraw()
    OnePlayerOval = Oval(Point(20,160),Point(190,230))
    OnePlayerOval.setFill('blue')
    OnePlayerOval.draw(Control)
    TwoPlayerOval = Oval(Point(210,160),Point(380,230))
    TwoPlayerOval.setFill('green')
    TwoPlayerOval.draw(Control)
    ZeroPlayerOval = Oval(Point(20,410),Point(190,480))
    ZeroPlayerOval.setFill('purple')
    ZeroPlayerOval.draw(Control)
    ZeroMSG = '0-Player'
    MS_MSG = 'Minesweeper'
    ZeroTXT = Text(Point(105,445),ZeroMSG)
    ZeroTXT.setStyle("bold")
    ZeroTXT.setFill("white")
    ZeroTXT.setSize(18)
    ZeroTXT.draw(Control)
    MSTXT = Text(Point(295,445),MS_MSG)
    MSTXT.setStyle("bold")
    MSTXT.setFill("white")
    MSTXT.setSize(18)
    MSOval = Oval(Point(210,410),Point(380,480))
    MSOval.setFill('pink3')
    MSOval.draw(Control)
    MSTXT.draw(Control)
    ExitRect = Rectangle(Point(130,290),Point(270,350))
    ExitRect.setFill('red')
    ExitRect.draw(Control)
    OnePlayer = "1-Player"
    TwoPlayer = "2-Player"
    Exit = "Exit"
    OnePlayerText = Text(Point(105,195),OnePlayer)
    OnePlayerText.setStyle("bold")
    OnePlayerText.setFill("white")
    OnePlayerText.setSize(18)
    OnePlayerText.draw(Control)
    TwoPlayerText = Text(Point(295,195),TwoPlayer)
    TwoPlayerText.setStyle("bold")
    TwoPlayerText.setFill("white")
    TwoPlayerText.setSize(18)
    TwoPlayerText.draw(Control)
    ExitText = Text(Point(200,320),Exit)
    ExitText.setStyle("bold")
    ExitText.setFill("white")
    ExitText.setSize(18)
    ExitText.draw(Control)
    # Returns the control panel window, the two ovals, and the exit rectangle
    return(Control,OnePlayerOval,TwoPlayerOval,ExitRect,ZeroPlayerOval,MSOval)

# defines gameboard function no args
def gameBoard():
    # Sets up all the gameboard elements
    Board = GraphWin("Game Board",600,600)
    Board.setBackground('white')
    Column1and2 = Line(Point(220,60),Point(220,540))
    Column2and3 = Line(Point(380,60),Point(380,540))
    Row1and2 = Line(Point(60,220),Point(540,220))
    Row2and3 = Line(Point(60,380),Point(540,380))
    Column1and2.setWidth(4)
    Column2and3.setWidth(4)
    Row1and2.setWidth(4)
    Row2and3.setWidth(4)
    Column1and2.draw(Board)
    Column2and3.draw(Board)
    Row1and2.draw(Board)
    Row2and3.draw(Board)
    TopMessage = "Your Turn Player 1"
    BottomMessage = "Click to Place a Marker"
    TopMessageText = Text(Point(300,30),TopMessage)
    BottomMessageText = Text(Point(300,570),BottomMessage)
    TopMessageText.setSize(16)
    BottomMessageText.setSize(16)
    TopMessageText.draw(Board)
    BottomMessageText.draw(Board)
    # Returns the gameboard window and the two messages
    return(Board,TopMessageText,BottomMessageText)

# defines check function 1 arg
def check(TicTacToeBoard):
    # messages and winline variable

    Xwins = "X wins the game!"
    Owins = "O wins the game!"
    WinLine = 0
    # Automatically makes the checkvalue variable false
    checkvalue = False

    # Checks each win condition (every combination where a winner could be declared) and changes the checkvalue variable to the correct winner
    # Also determines which line should be drawn (WinLine)
    if TicTacToeBoard[0] == "X" and TicTacToeBoard[1] == "X" and TicTacToeBoard[2] == "X":
        checkvalue = "X"
        WinLine = 1
        
    elif TicTacToeBoard[3] == "X" and TicTacToeBoard[4] == "X" and TicTacToeBoard[5] == "X":
        checkvalue = "X"
        WinLine = 2

    elif TicTacToeBoard[6] == "X" and TicTacToeBoard[7] == "X" and TicTacToeBoard[8] == "X":
        checkvalue = "X"
        WinLine = 3

    elif TicTacToeBoard[0] == "X" and TicTacToeBoard[3] == "X" and TicTacToeBoard[6] == "X":
        checkvalue = "X"
        WinLine = 4

    elif TicTacToeBoard[1] == "X" and TicTacToeBoard[4] == "X" and TicTacToeBoard[7] == "X":
        checkvalue = "X"
        WinLine = 5

    elif TicTacToeBoard[2] == "X" and TicTacToeBoard[5] == "X" and TicTacToeBoard[8] == "X":
        checkvalue = "X"
        WinLine = 6

    elif TicTacToeBoard[0] == "X" and TicTacToeBoard[4] == "X" and TicTacToeBoard[8] == "X":
        checkvalue = "X"
        WinLine = 7

    elif TicTacToeBoard[2] == "X" and TicTacToeBoard[4] == "X" and TicTacToeBoard[6] == "X":
        checkvalue = "X"
        WinLine = 8

    elif TicTacToeBoard[0] == "O" and TicTacToeBoard[1] == "O" and TicTacToeBoard[2] == "O":
        checkvalue = "O"
        WinLine = 1
        
    elif TicTacToeBoard[3] == "O" and TicTacToeBoard[4] == "O" and TicTacToeBoard[5] == "O":
        checkvalue = "O"
        WinLine = 2

    elif TicTacToeBoard[6] == "O" and TicTacToeBoard[7] == "O" and TicTacToeBoard[8] == "O":
        checkvalue = "O"
        WinLine = 3

    elif TicTacToeBoard[0] == "O" and TicTacToeBoard[3] == "O" and TicTacToeBoard[6] == "O":
        checkvalue = "O"
        WinLine = 4

    elif TicTacToeBoard[1] == "O" and TicTacToeBoard[4] == "O" and TicTacToeBoard[7] == "O":
        checkvalue = "O"
        WinLine = 5

    elif TicTacToeBoard[2] == "O" and TicTacToeBoard[5] == "O" and TicTacToeBoard[8] == "O":
        checkvalue = "O"
        WinLine = 6

    elif TicTacToeBoard[0] == "O" and TicTacToeBoard[4] == "O" and TicTacToeBoard[8] == "O":
        checkvalue = "O"
        WinLine = 7

    elif TicTacToeBoard[2] == "O" and TicTacToeBoard[4] == "O" and TicTacToeBoard[6] == "O":
        checkvalue = "O"
        WinLine = 8
        
    # If there is no winner, checkvalue will remain false
    else:
        checkvalue = False
    # Returns the winner value of checkvalue or False if there is no winner. Also returns the WinLine, which determines where the red line will be drawn
    return(checkvalue,WinLine)

# defines drawline function 2 args
def drawLine(WinLine,Board):
    # Based on the win line value, draws a line associated with it
    if WinLine == 1:
        Win = Line(Point(60,140),Point(540,140))
    elif WinLine == 2:
        Win = Line(Point(60,300),Point(540,300))
    elif WinLine == 3:
        Win = Line(Point(60,460),Point(540,460))
    elif WinLine == 4:
        Win = Line(Point(140,60),Point(140,540))
    elif WinLine == 5:
        Win = Line(Point(300,60),Point(300,540))
    elif WinLine == 6:
        Win = Line(Point(460,60),Point(460,540))
    elif WinLine == 7:
        Win = Line(Point(60,60),Point(540,540))
    elif WinLine == 8:
        Win = Line(Point(60,540),Point(540,60))
    
    # Color the line and set its width to 4 if a win has been reached
    if WinLine >= 1 and WinLine <= 8:
        Win.setWidth(4)
        Win.setOutline('red')
        Win.draw(Board)

# defines one player function
def onePlayer(Control,Board,TopMessageText,BottomMessageText,PlayerNames,Difficulty):

    playerInt = random.randint(1,2)
    
    if playerInt == 1:
        # Sets up list with spaces as the items in the list
        TicTacToeBoard = [' '] * 9
        turns = 0
        EXIT = 0
        
        if Difficulty == 0:
            # While exit has not been clicked
            while EXIT == 0:

                # Keep checking the mouse click within the control panel
                ClickControl = Control.checkMouse()

                # If there's a click, determine if it was in the exit box, if so, exit the loop
                if ClickControl != None:
                    ClickControlX = ClickControl.getX()
                    ClickControlY = ClickControl.getY()
                    if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                        EXIT = 1

                # Determines if it's player 1's turn and sets the proper messages and leters
                if turns%2 == 0:
                    letter = 'X'
                    TopMessage1 = "Your Turn " + PlayerNames[0]
                    TopMessageText.setText(TopMessage1)
                    BottomMessage1 = "Click to Place a Marker"
                    BottomMessageText.setText(BottomMessage1)
                    ClickBoard = Board.checkMouse()

                    # Keep going if there were no clicks
                    if ClickBoard == None:
                        continue

                    # If there was a click, check which box it was in
                    else:
                        ClickX = ClickBoard.getX()
                        ClickY = ClickBoard.getY()
                        
                    # If it was in one of the boxes and it was empty, if it is, place the letter there and mark it in the list
                        
                    if ClickX >= 60 and ClickX <= 220 and ClickY >= 60 and ClickY <=220:
                        if TicTacToeBoard[0] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[0] = letter
                            Marker = Text(Point(140,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 60 and ClickY <= 220:
                        if TicTacToeBoard[1] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[1] = letter
                            Marker = Text(Point(300,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 60 and ClickY <= 220:
                        if TicTacToeBoard[2] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[2] = letter
                            Marker = Text(Point(460,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 60 and ClickX <= 220 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[3] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[3] = letter
                            Marker = Text(Point(140,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                            

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[4] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[4] = letter
                            Marker = Text(Point(300,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1


                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[5] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[5] = letter
                            Marker = Text(Point(460,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 60 and ClickX <= 220 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[6] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[6] = letter
                            Marker = Text(Point(140,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[7] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[7] = letter
                            Marker = Text(Point(300,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[8] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[8] = letter
                            Marker = Text(Point(460,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                # If the letter is O, do the same as above
                    
                else:
                    letter = 'O'
                    TopMessage2 = "My Turn"
                    TopMessageText.setText(TopMessage2)
                    BottomMessage2 = "Thinking..."
                    BottomMessageText.setText(BottomMessage2)
                    TicTacToeBoardStr = ""
                    randomNum = random.randint(1,3)
                    sleep(randomNum)
                    x = True
                    while x:
                        ValueInt = random.randint(0,8)
                        if ValueInt == 0:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(140,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 1:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(300,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 2:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(460,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 3:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(140,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 4:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(300,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 5:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(460,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 6:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(140,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 7:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(300,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 8:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(460,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        else:
                            x = True

                
                # Run the check value function
                checkvalue,WinLine = check(TicTacToeBoard)
                # Run the draw line function
                drawLine(WinLine,Board)
                # If X or O wins, display the proper message, if neither win, call it a tie
                if checkvalue == "X":
                    WinMessage = PlayerNames[0] + " Wins!"
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
                elif checkvalue == "O":
                    WinMessage = "I Win!"
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
                elif turns == 9:
                    WinMessage = "It's a tie..."
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break

        elif Difficulty == 1:
            # While exit has not been clicked
            while EXIT == 0:

                # Keep checking the mouse click within the control panel
                ClickControl = Control.checkMouse()

                # If there's a click, determine if it was in the exit box, if so, exit the loop
                if ClickControl != None:
                    ClickControlX = ClickControl.getX()
                    ClickControlY = ClickControl.getY()
                    if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                        EXIT = 1

                # Determines if it's player 1's turn and sets the proper messages and leters
                if turns%2 == 0:
                    letter = 'X'
                    TopMessage1 = "Your Turn " + PlayerNames[0]
                    TopMessageText.setText(TopMessage1)
                    BottomMessage1 = "Click to Place a Marker"
                    BottomMessageText.setText(BottomMessage1)
                    ClickBoard = Board.checkMouse()

                    # Keep going if there were no clicks
                    if ClickBoard == None:
                        continue

                    # If there was a click, check which box it was in
                    else:
                        ClickX = ClickBoard.getX()
                        ClickY = ClickBoard.getY()
                        
                    # If it was in one of the boxes and it was empty, if it is, place the letter there and mark it in the list
                        
                    if ClickX >= 60 and ClickX <= 220 and ClickY >= 60 and ClickY <=220:
                        if TicTacToeBoard[0] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[0] = letter
                            Marker = Text(Point(140,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 60 and ClickY <= 220:
                        if TicTacToeBoard[1] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[1] = letter
                            Marker = Text(Point(300,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 60 and ClickY <= 220:
                        if TicTacToeBoard[2] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[2] = letter
                            Marker = Text(Point(460,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 60 and ClickX <= 220 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[3] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[3] = letter
                            Marker = Text(Point(140,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                            

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[4] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[4] = letter
                            Marker = Text(Point(300,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1


                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[5] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[5] = letter
                            Marker = Text(Point(460,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 60 and ClickX <= 220 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[6] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[6] = letter
                            Marker = Text(Point(140,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[7] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[7] = letter
                            Marker = Text(Point(300,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[8] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[8] = letter
                            Marker = Text(Point(460,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                # If the letter is O, do the same as above
                    
                else:
                    letter = 'O'
                    TopMessage2 = "My Turn"
                    TopMessageText.setText(TopMessage2)
                    BottomMessage2 = "Thinking..."
                    BottomMessageText.setText(BottomMessage2)
                    TicTacToeBoardStr = ""
                    randomNum = random.randint(1,3)
                    sleep(randomNum)
                    # Open the AI file
                    AIfile = open("AIPlayer2.txt","r")
                    # Iterate through the TicTacToeBoard and AI file, if they're equal, place a marker at the number in the string where specified
                    for ele in TicTacToeBoard:
                        TicTacToeBoardStr += ele
                    for line in AIfile:
                        line1 = line.split(":")
                        if TicTacToeBoardStr == line1[0]:
                            Value = line1[1].strip()
                            ValueInt = int(Value)
                            TicTacToeBoard[ValueInt] = letter
                            if ValueInt == 0:
                                Marker = Text(Point(140,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 1:
                                Marker = Text(Point(300,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 2:
                                Marker = Text(Point(460,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 3:
                                Marker = Text(Point(140,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 4:
                                Marker = Text(Point(300,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 5:
                                Marker = Text(Point(460,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 6:
                                Marker = Text(Point(140,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 7:
                                Marker = Text(Point(300,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 8:
                                Marker = Text(Point(460,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1

                
                # Run the check value function        
                checkvalue,WinLine = check(TicTacToeBoard)
                # Run the draw line function
                drawLine(WinLine,Board)
                # If X or O wins, display the proper message, if neither win, call it a tie
                if checkvalue == "X":
                    WinMessage = PlayerNames[0] + " Wins!"
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
                elif checkvalue == "O":
                    WinMessage = "I Win!"
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
                elif turns == 9:
                    WinMessage = "It's a tie..."
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
    elif playerInt == 2:
        # Sets up list with spaces as the items in the list
        TicTacToeBoard = [' '] * 9
        turns = 0
        EXIT = 0
        
        if Difficulty == 0:
            # While exit has not been clicked
            while EXIT == 0:

                # Keep checking the mouse click within the control panel
                ClickControl = Control.checkMouse()

                # If there's a click, determine if it was in the exit box, if so, exit the loop
                if ClickControl != None:
                    ClickControlX = ClickControl.getX()
                    ClickControlY = ClickControl.getY()
                    if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                        EXIT = 1

                # Determines if it's player 1's turn and sets the proper messages and leters
                if turns%2 == 0:
                    letter = 'X'
                    TopMessage2 = "My Turn"
                    TopMessageText.setText(TopMessage2)
                    BottomMessage2 = "Thinking..."
                    BottomMessageText.setText(BottomMessage2)
                    TicTacToeBoardStr = ""
                    randomNum = random.randint(1,3)
                    sleep(randomNum)
                    x = True
                    while x:
                        ValueInt = random.randint(0,8)
                        if ValueInt == 0:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(140,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 1:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(300,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 2:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(460,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 3:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(140,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 4:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(300,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 5:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(460,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 6:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(140,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 7:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(300,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        elif ValueInt == 8:
                            if TicTacToeBoard[ValueInt] != ' ':
                                continue
                            else:
                                Marker = Text(Point(460,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                                TicTacToeBoard[ValueInt] = letter
                                x = False
                        else:
                            x = True

                # If the letter is O, do the same as above
                    
                else:
                    letter = 'O'
                    TopMessage1 = "Your Turn " + PlayerNames[0]
                    TopMessageText.setText(TopMessage1)
                    BottomMessage1 = "Click to Place a Marker"
                    BottomMessageText.setText(BottomMessage1)
                    ClickBoard = Board.checkMouse()

                    # Keep going if there were no clicks
                    if ClickBoard == None:
                        continue

                    # If there was a click, check which box it was in
                    else:
                        ClickX = ClickBoard.getX()
                        ClickY = ClickBoard.getY()
                        
                    # If it was in one of the boxes and it was empty, if it is, place the letter there and mark it in the list
                        
                    if ClickX >= 60 and ClickX <= 220 and ClickY >= 60 and ClickY <=220:
                        if TicTacToeBoard[0] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[0] = letter
                            Marker = Text(Point(140,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 60 and ClickY <= 220:
                        if TicTacToeBoard[1] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[1] = letter
                            Marker = Text(Point(300,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 60 and ClickY <= 220:
                        if TicTacToeBoard[2] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[2] = letter
                            Marker = Text(Point(460,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 60 and ClickX <= 220 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[3] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[3] = letter
                            Marker = Text(Point(140,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                            

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[4] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[4] = letter
                            Marker = Text(Point(300,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1


                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[5] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[5] = letter
                            Marker = Text(Point(460,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 60 and ClickX <= 220 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[6] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[6] = letter
                            Marker = Text(Point(140,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[7] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[7] = letter
                            Marker = Text(Point(300,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[8] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[8] = letter
                            Marker = Text(Point(460,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                
                # Run the check value function        
                checkvalue,WinLine = check(TicTacToeBoard)
                # Run the draw line function
                drawLine(WinLine,Board)
                # If X or O wins, display the proper message, if neither win, call it a tie
                if checkvalue == "X":
                    WinMessage = "I Win!"
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
                elif checkvalue == "O":
                    WinMessage = PlayerNames[0] + " Wins!"
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
                elif turns == 9:
                    WinMessage = "It's a tie..."
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break

        elif Difficulty == 1:
            # While exit has not been clicked
            while EXIT == 0:

                # Keep checking the mouse click within the control panel
                ClickControl = Control.checkMouse()

                # If there's a click, determine if it was in the exit box, if so, exit the loop
                if ClickControl != None:
                    ClickControlX = ClickControl.getX()
                    ClickControlY = ClickControl.getY()
                    if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                        EXIT = 1

                # Determines if it's player 1's turn and sets the proper messages and leters
                if turns%2 == 0:
                    letter = 'X'
                    TopMessage2 = "My Turn"
                    TopMessageText.setText(TopMessage2)
                    BottomMessage2 = "Thinking..."
                    BottomMessageText.setText(BottomMessage2)
                    TicTacToeBoardStr = ""
                    randomNum = random.randint(1,3)
                    sleep(randomNum)
                    # Open the AI file
                    AIfile = open("AIPlayer2.txt","r")
                    # Iterate through the TicTacToeBoard and AI file, if they're equal, place a marker at the number in the string where specified
                    for ele in TicTacToeBoard:
                        TicTacToeBoardStr += ele
                    for line in AIfile:
                        line1 = line.split(":")
                        if TicTacToeBoardStr == line1[0]:
                            Value = line1[1].strip()
                            ValueInt = int(Value)
                            TicTacToeBoard[ValueInt] = letter
                            if ValueInt == 0:
                                Marker = Text(Point(140,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 1:
                                Marker = Text(Point(300,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 2:
                                Marker = Text(Point(460,140),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 3:
                                Marker = Text(Point(140,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 4:
                                Marker = Text(Point(300,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 5:
                                Marker = Text(Point(460,300),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 6:
                                Marker = Text(Point(140,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 7:
                                Marker = Text(Point(300,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1
                            elif ValueInt == 8:
                                Marker = Text(Point(460,460),letter)
                                Marker.setSize(34)
                                Marker.draw(Board)
                                turns = turns + 1

                # If the letter is O, do the same as above
                    
                else:
                    letter = 'O'
                    TopMessage1 = "Your Turn " + PlayerNames[0]
                    TopMessageText.setText(TopMessage1)
                    BottomMessage1 = "Click to Place a Marker"
                    BottomMessageText.setText(BottomMessage1)
                    ClickBoard = Board.checkMouse()

                    # Keep going if there were no clicks
                    if ClickBoard == None:
                        continue

                    # If there was a click, check which box it was in
                    else:
                        ClickX = ClickBoard.getX()
                        ClickY = ClickBoard.getY()
                        
                    # If it was in one of the boxes and it was empty, if it is, place the letter there and mark it in the list
                        
                    if ClickX >= 60 and ClickX <= 220 and ClickY >= 60 and ClickY <=220:
                        if TicTacToeBoard[0] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[0] = letter
                            Marker = Text(Point(140,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 60 and ClickY <= 220:
                        if TicTacToeBoard[1] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[1] = letter
                            Marker = Text(Point(300,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 60 and ClickY <= 220:
                        if TicTacToeBoard[2] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[2] = letter
                            Marker = Text(Point(460,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 60 and ClickX <= 220 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[3] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[3] = letter
                            Marker = Text(Point(140,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                            

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[4] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[4] = letter
                            Marker = Text(Point(300,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1


                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 220 and ClickY <= 380:
                        if TicTacToeBoard[5] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[5] = letter
                            Marker = Text(Point(460,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 60 and ClickX <= 220 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[6] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[6] = letter
                            Marker = Text(Point(140,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 220 and ClickX <= 380 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[7] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[7] = letter
                            Marker = Text(Point(300,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                    elif ClickX >= 380 and ClickX <= 540 and ClickY >= 380 and ClickY <= 540:
                        if TicTacToeBoard[8] != ' ': 
                            continue
                        else:
                            TicTacToeBoard[8] = letter
                            Marker = Text(Point(460,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1

                
                # Run the check value function        
                checkvalue,WinLine = check(TicTacToeBoard)
                # Run the draw line function
                drawLine(WinLine,Board)
                # If X or O wins, display the proper message, if neither win, call it a tie
                if checkvalue == "X":
                    WinMessage = "I Win!"
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
                elif checkvalue == "O":
                    WinMessage = PlayerNames[0] + " Wins!"
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
                elif turns == 9:
                    WinMessage = "It's a tie..."
                    TopMessageText.setText(WinMessage)
                    BottomText = "Click to close"
                    BottomMessageText.setText(BottomText)
                    break
    # Return the value of exit
    return(EXIT)


def twoPlayer(Control,Board,TopMessageText,BottomMessageText,PlayerNames):
    TicTacToeBoard = [' '] * 9
    turns = 0
    EXIT = 0

    # The code here is the same as the code for a one player game
    while EXIT == 0:

        ClickControl = Control.checkMouse()

        if ClickControl != None:
            ClickControlX = ClickControl.getX()
            ClickControlY = ClickControl.getY()
            if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                EXIT = 1
    
        if turns%2 == 0:
            letter = 'X'
            TopMessage1 = "Your Turn " + PlayerNames[0]
            TopMessageText.setText(TopMessage1)
            
        else:
            letter = 'O'
            TopMessage2 = "Your Turn " + PlayerNames[1]
            TopMessageText.setText(TopMessage2)

        ClickBoard = Board.checkMouse()
            
        if ClickBoard == None:
            continue

        else:
            ClickX = ClickBoard.getX()
            ClickY = ClickBoard.getY()
            
            
        if ClickX >= 60 and ClickX <= 220 and ClickY >= 60 and ClickY <=220:
            if TicTacToeBoard[0] != ' ': 
                continue
            else:
                TicTacToeBoard[0] = letter
                Marker = Text(Point(140,140),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1

        elif ClickX >= 220 and ClickX <= 380 and ClickY >= 60 and ClickY <= 220:
            if TicTacToeBoard[1] != ' ': 
                continue
            else:
                TicTacToeBoard[1] = letter
                Marker = Text(Point(300,140),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1

        elif ClickX >= 380 and ClickX <= 540 and ClickY >= 60 and ClickY <= 220:
            if TicTacToeBoard[2] != ' ': 
                continue
            else:
                TicTacToeBoard[2] = letter
                Marker = Text(Point(460,140),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1

        elif ClickX >= 60 and ClickX <= 220 and ClickY >= 220 and ClickY <= 380:
            if TicTacToeBoard[3] != ' ': 
                continue
            else:
                TicTacToeBoard[3] = letter
                Marker = Text(Point(140,300),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1
                

        elif ClickX >= 220 and ClickX <= 380 and ClickY >= 220 and ClickY <= 380:
            if TicTacToeBoard[4] != ' ': 
                continue
            else:
                TicTacToeBoard[4] = letter
                Marker = Text(Point(300,300),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1


        elif ClickX >= 380 and ClickX <= 540 and ClickY >= 220 and ClickY <= 380:
            if TicTacToeBoard[5] != ' ': 
                continue
            else:
                TicTacToeBoard[5] = letter
                Marker = Text(Point(460,300),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1

        elif ClickX >= 60 and ClickX <= 220 and ClickY >= 380 and ClickY <= 540:
            if TicTacToeBoard[6] != ' ': 
                continue
            else:
                TicTacToeBoard[6] = letter
                Marker = Text(Point(140,460),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1

        elif ClickX >= 220 and ClickX <= 380 and ClickY >= 380 and ClickY <= 540:
            if TicTacToeBoard[7] != ' ': 
                continue
            else:
                TicTacToeBoard[7] = letter
                Marker = Text(Point(300,460),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1

        elif ClickX >= 380 and ClickX <= 540 and ClickY >= 380 and ClickY <= 540:
            if TicTacToeBoard[8] != ' ': 
                continue
            else:
                TicTacToeBoard[8] = letter
                Marker = Text(Point(460,460),letter)
                Marker.setSize(34)
                Marker.draw(Board)
                turns = turns + 1
        checkvalue,WinLine = check(TicTacToeBoard)
        drawLine(WinLine,Board)
        if checkvalue == "X":
            WinMessage = PlayerNames[0] + " Wins!"
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
        elif checkvalue == "O":
            WinMessage = PlayerNames[1] + " Wins!"
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
        elif turns == 9:
            WinMessage = "It's a tie..."
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
    return(EXIT)


def ZeroPlayer(Control,Board,TopMessageText,BottomMessageText):
    TicTacToeBoard = [' '] * 9
    turns = 0
    EXIT = 0
    # While exit has not been clicked
    while EXIT == 0:

        # Keep checking the mouse click within the control panel
        ClickControl = Control.checkMouse()

        # If there's a click, determine if it was in the exit box, if so, exit the loop
        if ClickControl != None:
            ClickControlX = ClickControl.getX()
            ClickControlY = ClickControl.getY()
            if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                EXIT = 1

        # Determines if it's player 1's turn and sets the proper messages and leters
        if turns%2 == 0:
            letter = 'X'
            TopMessage2 = "Computer 1's Turn"
            TopMessageText.setText(TopMessage2)
            BottomMessage2 = "Thinking..."
            BottomMessageText.setText(BottomMessage2)
            TicTacToeBoardStr = ""
            randomNum = random.randint(1,3)
            sleep(randomNum)
            # Open the AI file
            AIfile = open("AIPlayer2.txt","r")
            # Iterate through the TicTacToeBoard and AI file, if they're equal, place a marker at the number in the string where specified
            for ele in TicTacToeBoard:
                TicTacToeBoardStr += ele
            for line in AIfile:
                line1 = line.split(":")
                if TicTacToeBoardStr == line1[0]:
                    Value = line1[1].strip()
                    ValueInt = int(Value)
                    TicTacToeBoard[ValueInt] = letter
                    if ValueInt == 0:
                        Marker = Text(Point(140,140),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 1:
                        Marker = Text(Point(300,140),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 2:
                        Marker = Text(Point(460,140),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 3:
                        Marker = Text(Point(140,300),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 4:
                        Marker = Text(Point(300,300),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 5:
                        Marker = Text(Point(460,300),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 6:
                        Marker = Text(Point(140,460),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 7:
                        Marker = Text(Point(300,460),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 8:
                        Marker = Text(Point(460,460),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
        else:
            letter = 'O'
            TopMessage2 = "Computer 2's Turn"
            TopMessageText.setText(TopMessage2)
            BottomMessage2 = "Thinking..."
            BottomMessageText.setText(BottomMessage2)
            TicTacToeBoardStr = ""
            randomNum = random.randint(1,3)
            sleep(randomNum)
            # Open the AI file
            AIfile = open("AIPlayer2.txt","r")
            # Iterate through the TicTacToeBoard and AI file, if they're equal, place a marker at the number in the string where specified
            for ele in TicTacToeBoard:
                TicTacToeBoardStr += ele
            for line in AIfile:
                line1 = line.split(":")
                if TicTacToeBoardStr == line1[0]:
                    Value = line1[1].strip()
                    ValueInt = int(Value)
                    TicTacToeBoard[ValueInt] = letter
                    if ValueInt == 0:
                        Marker = Text(Point(140,140),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 1:
                        Marker = Text(Point(300,140),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 2:
                        Marker = Text(Point(460,140),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 3:
                        Marker = Text(Point(140,300),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 4:
                        Marker = Text(Point(300,300),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 5:
                        Marker = Text(Point(460,300),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 6:
                        Marker = Text(Point(140,460),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 7:
                        Marker = Text(Point(300,460),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
                    elif ValueInt == 8:
                        Marker = Text(Point(460,460),letter)
                        Marker.setSize(34)
                        Marker.draw(Board)
                        turns = turns + 1
        checkvalue,WinLine = check(TicTacToeBoard)
        drawLine(WinLine,Board)
        # Uses check value to display the appropriate messages
        if checkvalue == "X":
            WinMessage = "Computer 1 Wins!"
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
        elif checkvalue == "O":
            WinMessage = "Computer 2 Wins!"
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
        elif turns == 9:
            WinMessage = "It's a tie..."
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
    # returns exit
    return(EXIT)
# defines settings
def settings():
    # defines the settings window
    Settings = GraphWin("                                     Settings", 400, 400)
    Settings.setBackground("Yellow")
    # creates the first rectangle
    rect1 = Rectangle(Point(10,10), Point(195,390))
    # sets the fill of the first rectangle
    rect1.setFill("black")
    # draws the first rectangle
    rect1.draw(Settings)
    # sets the 1st ext
    text1 = Text(Point(102.5, 200), "Easy")
    # sets color of text
    text1.setTextColor("white")
    # sets font
    text1.setFace("arial")
    # sets text size
    text1.setSize(30)
    # draws the second text
    text1.draw(Settings)
    # creates the second rectangle
    rect2 = Rectangle(Point(205,10), Point(390,390))
    # sets the fill of the second rectangle
    rect2.setFill("black")
    # draws the second rectangle
    rect2.draw(Settings)
    # sets the 2nd text
    text2 = Text(Point(297.5, 200), "Hard")
    # sets color of text
    text2.setTextColor("white")
    # sets font
    text2.setFace("arial")
    # sets text size
    text2.setSize(30)
    # draws the third text
    text2.draw(Settings)
    # returns objects
    return(Settings,rect1,rect2)
# defines minesweeper
def MineSweeper(Control,Board,TopMessageText,BottomMessageText):
    # initializes variables
    TicTacToeBoard = [' '] * 9
    turns = 0
    EXIT = 0
    mineblock = random.randint(0,8)
    mine = ' '
    # While exit has not been clicked
    while EXIT == 0:

        # Keep checking the mouse click within the control panel
        ClickControl = Control.checkMouse()

        # If there's a click, determine if it was in the exit box, if so, exit the loop
        if ClickControl != None:
            ClickControlX = ClickControl.getX()
            ClickControlY = ClickControl.getY()
            if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                EXIT = 1
        
        # Determines if it's player 1's turn and sets the proper messages and leters
        if turns%2 == 0:
            letter = 'X'
            TopMessage1 = "Your Turn Player 1"
            TopMessageText.setText(TopMessage1)
            BottomMessage1 = "Click to Place a Marker"
            BottomMessageText.setText(BottomMessage1)
            ClickBoard = Board.checkMouse()

            # Keep going if there were no clicks
            if ClickBoard == None:
                continue

            # If there was a click, check which box it was in
            else:
                ClickX = ClickBoard.getX()
                ClickY = ClickBoard.getY()

            # If it was in one of the boxes and it was empty, if it is, place the letter there and mark it in the list
            if ClickX >= 60 and ClickX <= 220 and ClickY >= 60 and ClickY <=220:
                if TicTacToeBoard[0] != ' ': 
                    continue
                elif mineblock == 0:
                    mine = 'X'
                else:
                    TicTacToeBoard[0] = letter
                    Marker = Text(Point(140,140),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1

            elif ClickX >= 220 and ClickX <= 380 and ClickY >= 60 and ClickY <= 220:
                if TicTacToeBoard[1] != ' ': 
                    continue
                elif mineblock == 1:
                    mine = 'X'
                else:
                    TicTacToeBoard[1] = letter
                    Marker = Text(Point(300,140),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1

            elif ClickX >= 380 and ClickX <= 540 and ClickY >= 60 and ClickY <= 220:
                if TicTacToeBoard[2] != ' ': 
                    continue
                elif mineblock == 2:
                    mine = 'X'
                else:
                    TicTacToeBoard[2] = letter
                    Marker = Text(Point(460,140),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1

            elif ClickX >= 60 and ClickX <= 220 and ClickY >= 220 and ClickY <= 380:
                if TicTacToeBoard[3] != ' ': 
                    continue
                elif mineblock == 3:
                    mine = 'X'
                else:
                    TicTacToeBoard[3] = letter
                    Marker = Text(Point(140,300),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1
                    

            elif ClickX >= 220 and ClickX <= 380 and ClickY >= 220 and ClickY <= 380:
                if TicTacToeBoard[4] != ' ': 
                    continue
                elif mineblock == 4:
                    mine = 'X'
                else:
                    TicTacToeBoard[4] = letter
                    Marker = Text(Point(300,300),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1


            elif ClickX >= 380 and ClickX <= 540 and ClickY >= 220 and ClickY <= 380:
                if TicTacToeBoard[5] != ' ': 
                    continue
                elif mineblock == 5:
                    mine = 'X'
                else:
                    TicTacToeBoard[5] = letter
                    Marker = Text(Point(460,300),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1

            elif ClickX >= 60 and ClickX <= 220 and ClickY >= 380 and ClickY <= 540:
                if TicTacToeBoard[6] != ' ': 
                    continue
                elif mineblock == 6:
                    mine = 'X'
                else:
                    TicTacToeBoard[6] = letter
                    Marker = Text(Point(140,460),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1

            elif ClickX >= 220 and ClickX <= 380 and ClickY >= 380 and ClickY <= 540:
                if TicTacToeBoard[7] != ' ': 
                    continue
                elif mineblock == 7:
                    mine = 'X'
                else:
                    TicTacToeBoard[7] = letter
                    Marker = Text(Point(300,460),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1

            elif ClickX >= 380 and ClickX <= 540 and ClickY >= 380 and ClickY <= 540:
                if TicTacToeBoard[8] != ' ': 
                    continue
                elif mineblock == 8:
                    mine = 'X'
                else:
                    TicTacToeBoard[8] = letter
                    Marker = Text(Point(460,460),letter)
                    Marker.setSize(34)
                    Marker.draw(Board)
                    turns = turns + 1

        # If the letter is O, do the same as above
            
        else:
            letter = 'O'
            TopMessage2 = "My Turn"
            TopMessageText.setText(TopMessage2)
            BottomMessage2 = "Thinking..."
            BottomMessageText.setText(BottomMessage2)
            TicTacToeBoardStr = ""
            randomNum = random.randint(1,3)
            sleep(randomNum)
            # Open the AI file
            AIfile = open("AIPlayer2.txt","r")
            # Iterate through the TicTacToeBoard and AI file, if they're equal, place a marker at the number in the string where specified
            for ele in TicTacToeBoard:
                TicTacToeBoardStr += ele
            # new conditions added from previous code that also have to pass through to make sure there isn't a mine block if clicked
            for line in AIfile:
                line1 = line.split(":")
                if TicTacToeBoardStr == line1[0]:
                    Value = line1[1].strip()
                    ValueInt = int(Value)
                    TicTacToeBoard[ValueInt] = letter
                    if ValueInt == 0:
                        if mineblock != 0:
                            Marker = Text(Point(140,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                        elif mineblock == 0:
                            mine = 'O'
                    elif ValueInt == 1:
                        if mineblock != 1:
                            Marker = Text(Point(300,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                        elif mineblock == 1:
                            mine = 'O'
                    elif ValueInt == 2:
                        if mineblock != 2:
                            Marker = Text(Point(460,140),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                        elif mineblock == 2:
                            mine = 'O'
                    elif ValueInt == 3:
                        if mineblock != 3:
                            Marker = Text(Point(140,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                        elif mineblock == 3:
                            mine = 'O'
                    elif ValueInt == 4:
                        if mineblock != 4:
                            Marker = Text(Point(300,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                        elif mineblock == 4:
                            mine = 'O'
                    elif ValueInt == 5:
                        if mineblock != 5:
                            Marker = Text(Point(460,300),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                        elif mineblock == 5:
                            mine = 'O'
                    elif ValueInt == 6:
                        if mineblock != 6:
                            Marker = Text(Point(140,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                        elif mineblock == 6:
                            mine = 'O'
                    elif ValueInt == 7:
                        if mineblock != 7:
                            Marker = Text(Point(300,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                    elif ValueInt == 8:
                        if mineblock != 8:
                            Marker = Text(Point(460,460),letter)
                            Marker.setSize(34)
                            Marker.draw(Board)
                            turns = turns + 1
                        elif mineblock == 8:
                            mine = 'O'

        
        # Run the check value function        
        checkvalue,WinLine = check(TicTacToeBoard)
        # Run the draw line function
        drawLine(WinLine,Board)
        # If X or O wins, display the proper message, if neither win, call it a tie
        if checkvalue == "X":
            WinMessage = "Player 1 Wins!"
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
        elif checkvalue == "O":
            WinMessage = "I Win!"
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
        elif turns == 9:
            WinMessage = "It's a tie..."
            TopMessageText.setText(WinMessage)
            BottomText = "Click to close"
            BottomMessageText.setText(BottomText)
            break
        # specifically for each mine block, if it is in the space that is clicked, explosion is drawn in this case forthe player
        elif mine != ' ':
            if mine == 'X':
                if mineblock == 0:
                    Explosion = Image(Point(140, 140), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 1:
                    Explosion = Image(Point(300, 140), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 2:
                    Explosion = Image(Point(460, 140), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 3:
                    Explosion = Image(Point(140, 300), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 4:
                    Explosion = Image(Point(300, 300), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 5:
                    Explosion = Image(Point(460, 300), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 6:
                    Explosion = Image(Point(140, 460), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 7:
                    Explosion = Image(Point(300, 460), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 8:
                    Explosion = Image(Point(460, 460), "Explosion.png")
                    Explosion.draw(Board)
            # custom names for messages
                WinMessage = "Player 1 Clicked the Mine, I Win!"
                TopMessageText.setText(WinMessage)
                BottomText = "Click to close"
                BottomMessageText.setText(BottomText)
                break
            # determines if computer clicked on a mine block
            elif mine == 'O':
                if mineblock == 0:
                    Explosion = Image(Point(140, 140), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 1:
                    Explosion = Image(Point(300, 140), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 2:
                    Explosion = Image(Point(460, 140), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 3:
                    Explosion = Image(Point(140, 300), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 4:
                    Explosion = Image(Point(300, 300), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 5:
                    Explosion = Image(Point(460, 300), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 6:
                    Explosion = Image(Point(140, 460), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 7:
                    Explosion = Image(Point(300, 460), "Explosion.png")
                    Explosion.draw(Board)
                elif mineblock == 8:
                    Explosion = Image(Point(460, 460), "Explosion.png")
                    Explosion.draw(Board)
                WinMessage = "Computer Clicked the Mine, Player 1 Wins!"
                TopMessageText.setText(WinMessage)
                BottomText = "Click to close"
                BottomMessageText.setText(BottomText)
                break
            # intializes random as true
        Random = True
        # randomly places mine in an empty space using while loop and condtionals
        while Random == True:
            mineblock = random.randint(0,8)
            if TicTacToeBoard[mineblock] != ' ':
                continue
            elif checkvalue != False:
                break
            else:
                break
    return(EXIT)

def main():
    # Set the exit controller to 0
    MainExit = 0
    # Run the control panel function
    Control,OnePlayerOval,TwoPlayerOval,ExitRect,ZeroPlayerOval,MSOval = controlPanel()
    Players = 0
    # While the exit button has not been clicked
    while MainExit == 0:
        # Keep checking if the mouse has been clicked, and determine if it was in an oval or rectangle
        GetClick = Control.getMouse()
        GetClickX = GetClick.getX()
        GetClickY = GetClick.getY()
        OnePlayerOvalC = OnePlayerOval.getCenter()
        OnePlayerOvalX = OnePlayerOvalC.getX()
        OnePlayerOvalY = OnePlayerOvalC.getY()
        Oval1Clicked = (((GetClickX - OnePlayerOvalX) ** 2 ) / (85 ** 2)) + (((GetClickY - OnePlayerOvalY) ** 2) / (35 ** 2))
        TwoPlayerOvalC = TwoPlayerOval.getCenter()
        TwoPlayerOvalX = TwoPlayerOvalC.getX()
        TwoPlayerOvalY = TwoPlayerOvalC.getY()
        ZeroPlayerOvalC = ZeroPlayerOval.getCenter()
        ZeroPlayerOvalX = ZeroPlayerOvalC.getX()
        ZeroPlayerOvalY = ZeroPlayerOvalC.getY()
        MSOvalC = MSOval.getCenter()
        MSOvalX = MSOvalC.getX()
        MSOvalY = MSOvalC.getY()
        Oval2Clicked = (((GetClickX - TwoPlayerOvalX) ** 2 ) / (85 ** 2)) + (((GetClickY - TwoPlayerOvalY) ** 2) / (35 ** 2))
        Oval3Clicked = (((GetClickX - ZeroPlayerOvalX) ** 2 ) / (85 ** 2)) + (((GetClickY - ZeroPlayerOvalY) ** 2) / (35 ** 2))
        Oval4Clicked = (((GetClickX - MSOvalX) ** 2 ) / (85 ** 2)) + (((GetClickY - MSOvalY) ** 2) / (35 ** 2))
        # If it was within the exit rectangle, exit and close the control panel
        if GetClickX >= 130 and GetClickX <= 270 and GetClickY >= 290 and GetClickY <= 350:
            MainExit = 1
            Control.close()

        # If it was in the one player oval, run the one player function
        elif Oval1Clicked <= 1:
            Players = 1
            SettingsClicked = 0
            Settings,rect1,rect2 = settings()
            while SettingsClicked == 0:
                EXIT = 0
                LocalEXIT = 0
                while LocalEXIT == 0:

                    ClickControl = Control.checkMouse()

                    if ClickControl != None:
                        ClickControlX = ClickControl.getX()
                        ClickControlY = ClickControl.getY()
                        if ClickControlX >= 130 and ClickControlX <= 270 and ClickControlY >= 290 and ClickControlY <= 350:
                            EnterButton = 1
                            LocalEXIT = 1
                    # checks for clicks to see if it can exit
                    Mouse = Settings.checkMouse()
                    if Mouse != None:
                        if checkpoint(Mouse,rect1):
                            Difficulty = 0
                            Settings.close()
                            SettingsClicked = 1
                            LocalEXIT = 2
                        elif checkpoint(Mouse,rect2):
                            Difficulty = 1
                            Settings.close()
                            SettingsClicked = 1
                            LocalEXIT = 2
                SettingsClicked = 1
                if LocalEXIT == 1:
                    EXIT = LocalEXIT
            if EXIT == 1:
                Settings.close()
                break
            PlayerNames,EXIT = KeyBoard(Players,Control)
            if EXIT == 1:
                break
            Board,TopMessageText,BottomMessageText = gameBoard()
            EXIT = onePlayer(Control,Board,TopMessageText,BottomMessageText,PlayerNames,Difficulty)
            # If exit was clicked, close everything
            if EXIT == 1:
                Board.close()
                Control.close()
                MainExit = 1
            # If it wasn't clicked, wait for either the window to close or for exit to be clicked
            else:
                MainExit2 = 0
                while MainExit2 == 0:
                    ConClick2 = Control.checkMouse()
                    click2 = Board.checkMouse()
                    if ConClick2 != None:
                        Click2X = ConClick2.getX()
                        Click2Y = ConClick2.getY()
                        if Click2X >= 130 and Click2X <= 270 and Click2Y >= 290 and Click2Y <= 350:
                            Board.close()
                            Control.close()
                            MainExit = 1
                    elif click2 != None:
                        Board.close()
                        MainExit2 = 1

        # If the two player oval was clicked, do the same as above
        elif Oval2Clicked <= 1:
            Players = 2
            PlayerNames,EXIT = KeyBoard(Players,Control)
            if EXIT == 1:
                break
            Board,TopMessageText,BottomMessageText = gameBoard()
            EXIT = twoPlayer(Control,Board,TopMessageText,BottomMessageText,PlayerNames)
            if EXIT == 1:
                Board.close()
                Control.close()
                MainExit = 1
            else:
                MainExit2 = 0
                while MainExit2 == 0:
                    ConClick2 = Control.checkMouse()
                    click2 = Board.checkMouse()
                    if ConClick2 != None:
                        Click2X = ConClick2.getX()
                        Click2Y = ConClick2.getY()
                        if Click2X >= 130 and Click2X <= 270 and Click2Y >= 290 and Click2Y <= 350:
                            Board.close()
                            Control.close()
                            MainExit = 1
                    elif click2 != None:
                        Board.close()
                        MainExit2 = 1
        elif Oval3Clicked <= 1:
            Board,TopMessageText,BottomMessageText = gameBoard()
            EXIT = ZeroPlayer(Control,Board,TopMessageText,BottomMessageText)
            # If exit was clicked, close everything
            if EXIT == 1:
                Board.close()
                Control.close()
                MainExit = 1
            # If it wasn't clicked, wait for either the window to close or for exit to be clicked
            else:
                MainExit2 = 0
                while MainExit2 == 0:
                    ConClick2 = Control.checkMouse()
                    click2 = Board.checkMouse()
                    if ConClick2 != None:
                        Click2X = ConClick2.getX()
                        Click2Y = ConClick2.getY()
                        if Click2X >= 130 and Click2X <= 270 and Click2Y >= 290 and Click2Y <= 350:
                            Board.close()
                            Control.close()
                            MainExit = 1
                    elif click2 != None:
                        Board.close()
                        MainExit2 = 1
        elif Oval4Clicked <= 1:
            Board,TopMessageText,BottomMessageText = gameBoard()
            EXIT = MineSweeper(Control,Board,TopMessageText,BottomMessageText)
            # checks for clicks to see if it can exit windows
            if EXIT == 1:
                Board.close()
                Control.close()
                MainExit = 1
            else:
                MainExit2 = 0
                while MainExit2 == 0:
                    ConClick2 = Control.checkMouse()
                    click2 = Board.checkMouse()
                    if ConClick2 != None:
                        Click2X = ConClick2.getX()
                        Click2Y = ConClick2.getY()
                        if Click2X >= 130 and Click2X <= 270 and Click2Y >= 290 and Click2Y <= 350:
                            Board.close()
                            Control.close()
                            MainExit = 1
                    elif click2 != None:
                        Board.close()
                        MainExit2 = 1
    # closes control
    Control.close()

# Run the main function
main()
