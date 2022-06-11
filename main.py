import turtle as t
import logging as log

def initBoard():
    board = [ #columns=7 rows=6
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], #row=0
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], #row=1
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], #row=2
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], #row=3
        [' ', ' ', ' ', ' ', ' ', ' ', ' '], #row=4
        [' ', ' ', ' ', ' ', ' ', ' ', ' '] #row=5
    ]#end board list

    return board
#end initBoard

def initTurtle():
    t.penup()
    t.speed(0)

def checkWinner(board, player):
    #check horizontal winners
    for row in range(6):
        for col in range(3):
            if(board[row][col] == player and 
                board[row][col+1] == player and
                board[row][col+2] == player and
                board[row][col+3] == player):
                return True
            #end if statement
        #end for col loop
    #end for row loop

    #check vertical winners
    for col in range(7):
        for row in range(3):
            if(board[row][col] == player and 
                board[row+1][col] == player and
                board[row+2][col] == player and
                board[row+3][col] == player):
                return True
            #end if statement
        #end for col loop
    #end for row loop

    #check diagonal winner
    for row in range(3):
        for col in range(4):
            if(board[row][col] == player and
                board[row+1][col+1] == player and
                board[row+2][col+2] == player and
                board[row+3][col+3] == player):
                return True
            #end if statement
        #end for col loop
    #end for row loop

    for row in range(3):
        for col in range(6):
            if(board[row][col] == player and
                board[row+1][col-1] == player and
                board[row+2][col-2] == player and
                board[row+3][col-3] == player):
                return True
            #end if statement
        #end for col loop
    #end for row loop

    return False
#end checkWinner

def placePiece(board, player, col):
    #for loop to put piece in column
    for row in range(6):
        if row == 5 and board[row][col] == ' ': #if last row
            board[row][col] = player
            break
    
        if board[row][col] == ' ': #check next
            if(board[row+1][col] != ' '): #check if column full
                board[row][col] = player
    
    displayBoards(board)
    return board
#end placePiece

def rectangle(width, height, center):
    log.debug("rectangle(" + str(width) + ", " + str(height) + ", " + str(center) + ")")

    t.penup()
    # t.speed(5)

    t.goto(center)

    #goto top left
    t.seth(90)
    t.fd(height/2)
    t.lt(90)
    t.fd(width/2)
    t.seth(0)

    #draw rectangle
    t.pendown()
    for i in range(2):
        t.fd(width)
        t.rt(90)
        t.fd(height)
        t.rt(90)
    
    log.debug("top right = " + str(t.pos()))
    log.info("center = " + str(center))

def fb(distance):
    t.fd(distance)
    t.bk(distance)

def makeLegs(boardWidth, boardHeight, boardCenter):
    log.debug("makeLegs(" + str(boardWidth) + ", " + str(boardHeight) + ", " + str(boardCenter) + ")")

    t.penup()
    # t.speed(5)

    t.goto(boardCenter)

    def makeLeg():
        t.pendown()
        
        #make left leg
        t.fd(boardHeight/10)
        t.rt(45)
        fb(boardHeight/10)
        t.lt(90)
        fb(boardHeight/10)
        t.seth(270)
        t.bk(boardHeight/10)
        t.seth(0)

        t.penup()

    #goto bottom left from center
    t.seth(270) #face down
    t.fd(boardHeight/2)
    t.rt(90)
    t.fd(boardWidth/2)
    t.seth(270) #face down
    
    makeLeg()

    #goto bottom right from left bottom
    t.fd(boardWidth)
    t.seth(270)

    makeLeg()

def drawGrid(width, height, center):
    rows = 6
    columns = 7

    t.penup()
    # t.speed(5)
    t.goto(center)

    #goto top left
    t.seth(90)
    t.fd(height/2)
    t.lt(90)
    t.fd(width/2)
    t.seth(0) #face right

    t.pendown()

    #draw vertical lines
    for i in range(columns):
        t.fd(width/columns)
        t.rt(90)
        if i < columns-1:
            fb(height)
        t.lt(90)
    
    #back to top left
    t.bk(width)

    #draw rows
    t.seth(270) #face down
    for i in range(rows):
        t.fd(height/rows)
        t.lt(90)
        if i < rows-1:
            fb(width)
        t.rt(90)

def drawBoard():
    #test normal
    width = 500
    height = 250

    #test small
    # width = 100
    # height = 50

    #test large
    # width = 1000
    # height = 500

    center = (0, 0) #must be a tuple

    log.debug("drawBoard(" + str(width) + ", " + str(height) + ", " + str(center) + ")")

    rectangle(width, height, center) #outline of main board
    makeLegs(boardWidth=width, boardHeight=height, boardCenter=center)
    drawGrid(width, height, center)

def displayBoards(board):
    turtleprintBoard(board)
    terminalPrintBoard(board)

def turtleprintBoard(board):
    print("hi")
    drawBoard()

def terminalPrintBoard(board):
    for row in range(6):
        print("[ ", end="")
        for col in range(7):
            print(board[row][col], end=" ")
            if(col != 6):
                print("| ", end="")
            #end if statement - for spacer
        #end for col loop
        if row != 6:
            print("]\n", end="")
        else:
            print("]", end="")
    #end for row loop

    print("-----------------------------")
    print("| 0 | 1 | 2 | 3 | 4 | 5 | 6 |")
    print("-----------------------------")
    print(" |                         | ")
    print("/ \\                       / \\ \n")
#end printBoard(board)

def playGame(board):
    displayBoards(board)

    turn = 'g' #either g->green, a->azul
    winner = False
    while not winner:
        #user choose column 
        print("Which column?")
        userInput = input()
        col = int(userInput) #between 0-6

        placePiece(board, turn, col)
        
        displayBoards(board)
        winner = checkWinner(board, turn)
        if winner:
            print("\n\nWINNNER\n\n")
        
        #switch whos turn it is
        if turn == 'g':
            turn = 'a'
        #end if statement
        else:
            turn = 'g'
        #end else statement
    #end while loop

def main():
    log.basicConfig(level=log.DEBUG, filename="main.log", filemode='w')
    initTurtle()
    board = initBoard()
    
    print("Welcome to Connect 4 python edition! To win you have to well... connect 4 spaces in any direction")
    
    turtleprintBoard(board)
    # playGame()
    
    done = input("close game")
    t.done()


main()