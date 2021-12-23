from tkinter import *
import time 

board = {1:' ',2:' ',3:' ',
         4:' ',5:' ',6:' ',
         7:' ',8:' ',9:' '}

global player1
player1 = True
global player2
player2 = True
global count 
count = 0

def first_button():
    global player1
    global player2
    global count

    if player1 is True and board[1] == ' ':
        button1.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[1] = 'X'
        count = count + 1
    elif player2 is True and board[1] == ' ':
        button1.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[1] = 'O'
        count = count + 1
    else:
        print('already taken')
    
    print(count)
    check_winner()

def second_button():
    global player1
    global player2 
    global count

    if player1 is True and board[2] == ' ':
        button2.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[2] = 'X'
        count = count + 1
    elif player2 is True and board[2] == ' ':
        button2.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[2] = 'O'
        count = count + 1
    else:
        print('already taken')
    print(count)
    check_winner()

def third_button():
    global player1
    global player2
    global count

    if player1 is True and board[3] == ' ':
        button3.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[3] = 'X'
        count = count + 1
    elif player2 is True and board[3] == ' ':
        button3.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[3] = 'O'
        count = count + 1

    print(count)
    check_winner()

def fourth_button():
    global player1
    global player2
    global count

    if player1 is True and board[4] == ' ':
        button4.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[4] = 'X'
        count = count + 1
    elif player2 is True and board[4] == ' ':
        button4.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[4] = 'O'
        count = count + 1

    print(count)
    check_winner()

def fifth_button():
    global player1
    global player2
    global count

    if player1 is True and board[5] == ' ':
        button5.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[5] = 'X'
        count = count + 1
    elif player2 is True and board[5] == ' ':
        button5.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[5] = 'O'
        count = count + 1

    print(count)
    check_winner()

def sixth_button():
    global player1
    global player2
    global count

    if player1 is True and board[6] == ' ':
        button6.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[6] = 'X'
        count = count + 1
    elif player2 is True and board[6] == ' ':
        button6.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[6] = 'O'
        count = count + 1

    print(count)
    check_winner()

def seventh_button():
    global player1
    global player2
    global count

    if player1 is True and board[7] == ' ':
        button7.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[7] = 'X'
        count = count + 1
    elif player2 is True and board[7] == ' ':
        button7.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[7] = 'O'
        count = count + 1

    print(count)
    check_winner()

def eight_button():
    global player1
    global player2
    global count

    if player1 is True and board[8] == ' ':
        button8.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[8] = 'X'
        count = count + 1
    elif player2 is True and board[8] == ' ':
        button8.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[8] = 'O'
        count = count + 1
    else:
        print('already taken')
    
    print(count)
    check_winner()

def ninth_button():
    global player1
    global player2
    global count

    if player1 is True and board[9] == ' ':
        button9.config(text = 'X', bg = 'gray')
        player2 = True
        player1 = False
        board[9] = 'X'
        count = count + 1
    elif player2 is True and board[9] == ' ':
        button9.config(text = 'O', bg = 'gray')
        player1 = True
        player2 = False
        board[9] = 'O'
        count = count + 1
    else:
        print('already taken')
    
    print(count)
    check_winner()

def check_winner():

    global player1
    global player2
    if board[1] == board[2] == board[3]:
        if board[1] == board[2] == board[3] == 'X':
            button1.config(bg = 'green')
            button2.config(bg = 'green')
            button3.config(bg = 'green') 
            winner_label.config(text = 'X Win')
            player1 = False
            player2 = False
        elif board[1] == board[2] == board[3] == 'O':
            button1.config(bg = 'red')
            button2.config(bg = 'red')
            button3.config(bg = 'red')
            winner_label.config(text = 'O Win')
            player1 = False
            player2 = False


    elif board[4] == board[5] == board[6]:
        if board[4] == board[5] == board[6] == 'X':
            button4.config(bg = 'green')
            button5.config(bg = 'green')
            button6.config(bg = 'green') 
            winner_label.config(text = 'X Win')
            player1 = False
            player2 = False
        elif board[4] == board[5] == board[6] == 'O':
            button4.config(bg = 'red')
            button5.config(bg = 'red')
            button6.config(bg = 'red')
            winner_label.config(text = 'O Win')
            player1 = False
            player2 = False
        
    elif board[7] == board[8] == board[9]:
        if board[7] == board[8] == board[9] == 'X': 
            button7.config(bg = 'green')
            button8.config(bg = 'green')
            button9.config(bg = 'green')
            winner_label.config(text = 'X Win')
            player1 = False
            player2 = False
        elif board[7] == board[8] == board[9] == 'O':
            button7.config(bg = 'red')
            button8.config(bg = 'red')
            button9.config(bg = 'red') 
            winner_label.config(text = 'O Win')
            draw_frame.grid(row = 0)
            player1 = False
            player2 = False
        

    elif board[1] == board[5] == board[9]:
        if board[1] == board[5] == board[9] == 'X':
            button1.config(bg = 'green')
            button5.config(bg = 'green')
            button9.config(bg = 'green') 
            winner_label.config(text = 'X Win')
            player1 = False
            player2 = False
        elif board[1] == board[5] == board[9] == 'O':
            button1.config(bg = 'red')
            button5.config(bg = 'red')
            button9.config(bg = 'red') 
            winner_label.config(text = 'O Win')
            player1 = False
            player2 = False
        

    elif board[3] == board[5] == board[7]:
        if board[3] == board[5] == board[7] == 'X':
            button3.config(bg = 'green')
            button5.config(bg = 'green')
            button7.config(bg = 'green')
            winner_label.config(text = 'X Win')
            player1 = False
            player2 = False
        elif board[3] == board[5] == board[7] == 'O':
            button3.config(bg = 'red')
            button5.config(bg = 'red')
            button7.config(bg = 'red')
            winner_label.config(text = 'O Win')
            player1 = False
            player2 = False

    elif board[1] == board[4] == board[7]:
        if board[1] == board[4] == board[7] == 'X':
            button1.config(bg = 'green')
            button4.config(bg = 'green')
            button7.config(bg = 'green') 
            winner_label.config(text = 'X Win')
            player1 = False
            player2 = False
        elif board[1] == board[4] == board[7] == 'O':
            button1.config(bg = 'red')
            button4.config(bg = 'red')
            button7.config(bg = 'red') 
            winner_label.config(text = 'O Win')
            player1 = False
            player2 = False

    elif board[2] == board[5] == board[8]:
        if board[2] == board[5] == board[8] == 'X':
            button2.config(bg = 'green')
            button5.config(bg = 'green')
            button8.config(bg = 'green') 
            winner_label.config(text = 'X Win')
            player1 = False
            player2 = False
        elif board[2] == board[5] == board[8] == 'O':
            button2.config(bg = 'red')
            button5.config(bg = 'red')
            button8.config(bg = 'red') 
            winner_label.config(text = ' Win')
            player1 = False
            player2 = False

    elif board[3] == board[6] == board[9]:
        if board[3] == board[6] == board[9] == 'X':
            button3.config(bg = 'green')
            button6.config(bg = 'green')
            button9.config(bg = 'green')
            winner_label.config(text = 'X Win')
            player1 = False
            player2 = False
        elif board[3] == board[6] == board[9] == 'O':
            button3.config(bg = 'red')
            button6.config(bg = 'red')
            button9.config(bg = 'red')
            winner_label.config(text = 'O Win')
            player1 = False
            player2 = False
        
    elif count == 7:
        winner_label.config(text = 'Draw')
        button1.config(bg = 'red')
        button2.config(bg = 'red')
        button3.config(bg = 'red')
        button4.config(bg = 'red')
        button5.config(bg = 'red')
        button6.config(bg = 'red')
        button7.config(bg = 'red')
        button8.config(bg = 'red')
        button9.config(bg = 'red')
        player1 = False
        player2 = False
        

def clear_all():

    global count
    global player1
    global player2

    winner_label.config(text = ' ')
    player1 = True
    player2 = False
    count = 0
    board[1] = ' '
    board[2] = ' '
    board[3] = ' '
    board[4] = ' '
    board[5] = ' '
    board[6] = ' '
    board[7] = ' '
    board[8] = ' '
    board[9] = ' '
    button1.config(text = ' ', bg = 'black')
    button2.config(text = ' ', bg = 'black')
    button3.config(text = ' ', bg = 'black')
    button4.config(text = ' ', bg = 'black')
    button5.config(text = ' ', bg = 'black')
    button6.config(text = ' ', bg = 'black')
    button7.config(text = ' ', bg = 'black')
    button8.config(text = ' ', bg = 'black')
    button9.config(text = ' ', bg = 'black')


root = Tk()

center_frame = Frame(width = 150, height = 600)
bottom_frame = Frame(width = 150, height = 600)

center_frame.grid(column = 1, row = 0)
bottom_frame.grid(column = 1, row = 1)

#center frame
board_frame = Frame(center_frame)
board_frame.grid(row = 0)

button1 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white', width = 3, command = first_button)
button2 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white', width = 3, command = second_button)
button3 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white',width = 3, command = third_button)

button4 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white',width = 3, command = fourth_button)
button5 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white',width = 3, command = fifth_button)
button6 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white',width = 3, command = sixth_button)

button7 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white', width = 3, command = seventh_button)
button8 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white',width = 3, command = eight_button)
button9 = Button(board_frame, text = '',font = ('arial rounded mt', 37), bg = 'black', fg = 'white',width = 3, command = ninth_button)

button1.grid(column = 0, row = 0)
button2.grid(column = 1, row = 0)
button3.grid(column = 2, row = 0)

button4.grid(column = 0, row = 1)
button5.grid(column = 1, row = 1)
button6.grid(column = 2, row = 1)

button7.grid(column = 0, row = 2)
button8.grid(column = 1, row = 2)
button9.grid(column = 2, row = 2)


winner_label = Label(bottom_frame,text = '', font = ('Showcard gothic', 15))
winner_label.grid(row = 0)

new_game_button = Button(bottom_frame, text = 'New Game', font = ('showcard gothic', 15), command = clear_all)
new_game_button.grid(row = 1)

root.mainloop()
