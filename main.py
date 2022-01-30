import math

def isinrow (board, gridsize, row, trynum): # check if guess number is in the selected row
    for i in range(gridsize):
        if board[row][i] == trynum:
            return True
    return False

def isincol(board, gridsize, col, trynum): # check if guess number is in the selected column
    for i in range(gridsize):
        if board[i][col] == trynum:
            return True
    return False

def isinbox(board, gridsize, row, col, trynum): # check if guess number is in box of selected row and column
    for i in range(gridsize): # get row of upper left of box
        check = row%math.sqrt(gridsize)
        if not check:
            break
        else:
            row = row-1
    for i in range(gridsize): # get col of upper left of box
        check = col%math.sqrt(gridsize)
        if not check:
            break
        else:
            col =  col-1

    for i in range(int(math.sqrt(gridsize))): #row
        for j in range(int(math.sqrt(gridsize))): #col
            if trynum == board[row+i][col+j]: # check each box
                return True
    return False

def isvalidplacement(board, gridsize, row, col, trynum):
    if (not isinrow(board, gridsize, row, trynum) and
        not isincol(board, gridsize, col, trynum) and
        not isinbox(board, gridsize, row, col, trynum)):
        return True
    else:
        return False

def solvepuz(board, gridsize):
    for i in range(gridsize): #cycle through row
        for j in range(gridsize): # cycle through col
            if board[i][j] == 0: # if there is an empty spot
                for trynum in range(1,gridsize+1): # try numbers 1-9
                    if isvalidplacement(board, gridsize, i, j, trynum): # if we can place the number
                        board[i][j] = trynum #put number in to open slot
                        if solvepuz(board, gridsize): # if we can still solve
                            return True # keep going
                        else: # otherwise leave it blank
                            board[i][j]=0
                return False # not solvable with current set of numbers
    return True # fully solved

def printboard (board, gridsize):
    for i in range(gridsize):
        for j in range(gridsize):
            if j == gridsize - 1:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")


# --------Start of main function--------

# Get grid size for board
gridsize = int(input('Enter row or column length of Sudoku puzzle: '))
print()
board = [[0] * gridsize for i in range(gridsize)] #initialize board space

# Enter grid from user (1-9 in puzzle, 0 not in puzzle)

for i in range(gridsize):
    row_input = input('Enter row '+ str(i+1) + ' of Sudoku puzzle. Use 0 for empty slots. Ex: 1 3 4 (3x3 puzzle): ')
    col = 0
    for j in range(2*gridsize):
        if not (j%2):
            board[i][col] = int(row_input[j])
            col += 1

# board = [ # test board
#    [5,0,0,0,7,0,0,0,4],
#    [6,0,9,0,3,1,0,5,0],
#    [8,0,0,0,0,9,0,1,0],
#    [4,9,0,1,0,0,8,0,2],
#    [2,0,8,0,0,6,7,0,5],
#    [0,0,0,2,8,4,1,0,0],
#    [0,7,4,0,0,8,5,6,0],
#    [1,0,0,7,6,3,4,2,0],
#    [9,6,0,0,0,0,0,0,0]
#]

# Show user input
print()
print('Sudoku Puzzle Input:')
printboard(board, gridsize)

# Display solved board or return that it cannot be solved
if solvepuz(board, gridsize):
    print()
    print('Sudoku Puzzle Output:')
    printboard(board, gridsize)
else:
    print()
    print("Cannot Solve Puzzle")

input()