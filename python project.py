import copy
from pprint import pprint

# words that appear include: "buzz", "dank", "gains", "protein", "vibe", "chad"
word_board0 = [["j", "c", "e", "l", "s", "r", "w", "l", "r", "y", "n", "h"],
               ["f", "q", "e", "n", "c", "p", "k", "s", "i", "k", "m", "s"],
               ["a", "u", "d", "h", "t", "i", "r", "r", "t", "q", "g", "l"],
               ["x", "x", "k", "k", "c", "n", "d", "o", "n", "q", "b", "v"],
               ["y", "g", "n", "t", "t", "p", "b", "a", "t", "m", "v", "r"],
               ["q", "j", "x", "u", "k", "s", "v", "u", "n", "e", "d", "f"],
               ["x", "m", "q", "p", "n", "a", "j", "q", "z", "k", "i", "c"],
               ["l", "x", "u", "k", "h", "f", "g", "s", "r", "z", "s", "n"],
               ["i", "g", "f", "s", "x", "d", "c", "a", "q", "i", "h", "c"],
               ["b", "r", "z", "t", "p", "l", "v", "d", "i", "i", "z", "h"],
               ["n", "h", "v", "t", "r", "f", "i", "s", "i", "n", "m", "a"],
               ["q", "a", "o", "n", "v", "i", "b", "e", "v", "q", "s", "d"]]
               
# words that appear include: "yeet", "woke", "swag", "gang"
word_board1 = [["y", "e", "e", "t", "i", "w"],
              ["f", "k", "p", "e", "w", "o"],
              ["g", "n", "a", "g", "r", "k"],
              ["e", "a", "s", "a", "i", "e"],
              ["z", "h", "w", "j", "r", "q"],
              ["p", "o", "u", "s", "k", "x"]]

# words that appear include: "flop"
word_board2 = [["f", "x", "u", "e"],
               ["i", "l", "k", "q"],
               ["p", "w", "o", "m"],
               ["d", "s", "x", "p"]]

# words that appear include: "tea", "yet"
word_board3 = [["y", "t", "s"],
               ["d", "e", "k"],
               ["m", "a", "t"]]

def rotate_board_90(word_board):
    '''(list) -> (list)
    Returns the word board rotated count-clockwise 90 degrees so that the 
    lists that appear at the last column in the word board are returned as 
    the first line in the list of lists
    
    >>> rotate_board_90(word_board2)
    [['e', 'q', 'm', 'p'], ['u', 'k', 'o', 'x'], ['x', 'l', 'w', 's'], ['f', 'i'
    , 'p', 'd']]
    '''
    # determines number of columns
    number_columns = len(word_board[0])
    # creates new empty lists to be added to in the future
    rotated_board = []
    new_row = []
    count = 0
    # takes the last column of the list of list and turns it to the first row
    # repeats for all columns
    while (count < number_columns):
        for index in range(number_columns):
            new_row.append(word_board[index][number_columns-count-1])
        count += 1
        # addes new rows together in a list
        rotated_board.append(new_row)
        new_row = []
    return rotated_board

def word_to_list(word):
    ''' (str) -> (list)
    Turns the entered string word into a list
    
    >>> word_to_list("yeet")
    ['y', 'e', 'e', 't']
    '''
    # takes a string and changes it to a list
    list_word = list(word)
    return list_word
        
def read_lr(row, word):
    '''(list, str) -> (bool)
    Determines if word is in a row of letters by searching each row in order 
    from left to right
    
    >>> read_lr(['y', 'e', 'e', 't'], "yeet")
    True
    '''
    # changes string to list
    list_word = word_to_list(word)
    # searches for list in a row of the list of list
    for index in range(len(row) - len(list_word)+1):
        for mark in range(len(list_word)):
            # THIS CODE BELOW IS FROM STACK OVERFLOW
            if row[index + mark] != list_word[mark]:
                # stops code when list is found in row and returns True
                break
        else:
            return True
    return False
# THIS CODE ABOVE IS FROM STACK OVERFLOW
def appear_lr(word_board, word):
    '''(list, str) -> (bool)
    Determines if word appears in the word board as if read left to right 
    throughout all rows in word board
    
    >>> appear_lr(word_board3, "tea")
    False 
    >>> appear_lr(word_board1, "yeet")
    True
    '''
    # determines number of rows
    number_rows = len(word_board)
    row = 0
    # goes through each row of the list of list and finds if word is contained
    # inside of a row
    while (row < number_rows):
        find = read_lr(word_board[row], word)
        if find == True:
            return True        
        row += 1
    else:
        return False
    
def appear_hori_vert(word_board, word):
    '''(list, str) -> (str)
    Determines if word appears in all directions horizontal and vertical
    
    >>> appear_hori_vert(word_board1, "gang")
    True
    '''
    # creates a shallow copy of the list of list rotated to all 4 horizontal
    # and vertical directions
    board_tb = rotate_board_90(word_board)
    board_rl = rotate_board_90(board_tb)
    board_bt = rotate_board_90(board_rl)
    # checks each direction if the word is contained in that direction
    found_lr = appear_lr(word_board, word)
    found_tb = appear_lr(board_tb, word)
    found_rl = appear_lr(board_rl, word)
    found_bt = appear_lr(board_bt, word)
    # if the word appears at least once, returns true
    return found_lr or found_tb or found_rl or found_bt

def flipper(word_board):
    '''(list) -> (list)
    Returns the word board as if the lists were read from right to left
    without changing the order the lists were originally in
    
    >>> flipper(word_board2)
    [['e', 'u', 'x', 'f'], ['q', 'k', 'l', 'i'], ['m', 'o', 'w', 'p'], ['p', 
    'x', 's', 'd']]
    '''
    # creates empty list for future inputs
    rotated_board = []
    # goes through every row in the list of list and reveres it to read right to
    # left
    for i in word_board:
        i.reverse()
        # addes that newly reversed row to an empty list
        rotated_board.append(i)
    return rotated_board

def rotate_diagonalSE_part1(word_board):
    '''(list) -> (list)
    Rotates the first half of the board to the SE direction
    
    >>> rotate_diagonalSE_part1(word_board2)
    [['f'], ['x', 'i'], ['u', 'l', 'p'], ['e', 'k', 'w', 'd']]
    '''
    # finds the number of columns
    number_columns = len(word_board[0])
    # creates an empty list for the final output list of list
    rotated_board = []
    new_row = []
    # goes through each column and selects specific letters for the list
    for i in range (number_columns):
        new_row.append(word_board[0][number_columns-i-1])
        for j in range (i):
            new_row.append(word_board[j+1][number_columns-i+j])
        # creates new list of list with diagonal letters going SE
        rotated_board.append(new_row)
        new_row = []
    return rotated_board

def rotate_diagonalSE_part2(word_board):
    '''(list) -> (list)
    Rotates the second half of the board in the SE direction
    
    >>> rotate_diagonalSE_part2(word_board2)
    [['q', 'o', 's'], ['m', 'x'], ['p']]
    '''
    # finds the number of columns
    number_columns = len(word_board[0])
    # creates an empty list for the final output list of list
    rotated_board = []
    new_row = []
    # goes through each column and selects specific letters for the list
    for i in range (number_columns-1):
        for j in range (number_columns-1-i, 0, -1):
            new_row.append(word_board[number_columns-j][number_columns-j-1-i])
        # creates new list of list with diagonal letters going SE
        rotated_board.append(new_row)
        new_row = []
    return rotated_board

def rotate_diagonalSE(word_board):
    '''(list) -> (list)
    Rotates the whole board in the SE direction
    
    >>> rotate_diagonalSE(word_board2)
    [['e'], ['u', 'q'], ['x', 'k', 'm'], ['f', 'l', 'o', 'p'], ['i', 'w', 'x'], 
    ['p', 's'], ['d']]
    '''
    # combines the list of list from the first half of the board with the second
    # half of the board in the SE direction
    first_half = rotate_diagonalSE_part1(word_board)
    second_half = rotate_diagonalSE_part2(word_board)
    SE = first_half + second_half
    return SE

def rotate_diagonalNW(word_board):
    '''(list) -> (list)
    Rotates the whole board in the NW direction
    
    >>> rotate_diagonalNW(word_board2)
    [['e'], ['q', 'u'], ['m', 'k', 'x'], ['p', 'o', 'l', 'f'], ['x', 'w', 'i'], 
    ['s', 'p'], ['d']]
    '''
    # copies the list in the SE direction and changes it to the NW direction by
    # flipping it 180 degrees
    new_list = word_board.copy()
    NW = flipper(rotate_diagonalSE(new_list))
    return NW

def rotate_diagonalSW_part1(word_board):
    '''(list) -> (list)
    Rotates the first half of the board in the SW direction
    
    >>> rotate_diagonalSW_part1(word_board2)
    [['f'], ['x', 'i'], ['u', 'l', 'p'], ['e', 'k', 'w', 'd']]
    '''
    # finds the number of columns
    number_columns = len(word_board[0])
    # creates an empty list for the final output list of list
    rotated_board = []
    new_row = []
    # goes through each column and selects specific letters for the list
    for i in range (number_columns):
        new_row.append(word_board[0][i])
        for j in range (i):
            new_row.append(word_board[j+1][i-1-j])
        # creates new list of list with diagonal letters going SW
        rotated_board.append(new_row)
        new_row = []
    return rotated_board
    
def rotate_diagonalSW_part2(word_board):
    '''(list) -> (list)
    Rotates the second half of the board in the SW direction
    
    >>> rotate_diagonalSW_part2(word_board2)
    [['q', 'o', 's'], ['m', 'x'], ['p']]
    '''
    # finds the number of columns
    number_columns = len(word_board[0])
    # creates an empty list for the final output list of list
    rotated_board = []
    new_row = []
    # goes through each column and selects specific letters for the list
    for i in range (number_columns-1):
        for j in range (number_columns-1-i, 0, -1):
            new_row.append(word_board[number_columns-j][j+i])
        # creates new list of list with diagonal letters going SW
        rotated_board.append(new_row)
        new_row = []
    return rotated_board

def rotate_diagonalSW(word_board):
    '''(list) -> (list)
    Rotates the whole board in the SW direction
    
    >>> rotate_diagonalSW(word_board2)
    [['f'], ['x', 'i'], ['u', 'l', 'p'], ['e', 'k', 'w', 'd'], ['q', 'o', 's'],
    ['m', 'x'], ['p']]
    '''
    # combines the list of list from the first half of the board with the second
    # half of the board in the SW direction    
    first_half = rotate_diagonalSW_part1(word_board)
    second_half = rotate_diagonalSW_part2(word_board)
    SW = first_half + second_half
    return SW

def rotate_diagonalNE(word_board):
    '''(list) -> (list)
    Rotates the whole board in the NE direction
    
    >>> rotate_diagonalNE(word_board2)
    ['f'], ['i', 'x'], ['p', 'l', 'u'], ['d', 'w', 'k', 'e'], ['s', 'o', 'q'],
    ['x', 'm'], ['p']]
    '''
    # copies the list in the SW direction and changes it to the NE direction by
    # flipping it 180 degrees    
    new_list = word_board.copy()
    NE = flipper(rotate_diagonalSW(new_list))
    return NE

def appear_diagonals(word_board, word):
    '''(list, str) -> (bool)
    Determines if word appears in all diagonal directions
    
    >>> appear_diagonals(word_board3, "tea")
    False
    '''
    # goes through the list of list in all diagonal directions and searches for 
    # word
    found_SE = appear_lr(rotate_diagonalSE(word_board), word)
    found_NW = appear_lr(rotate_diagonalNW(word_board), word)
    found_SW = appear_lr(rotate_diagonalSW(word_board), word)
    found_NE = appear_lr(rotate_diagonalNE(word_board), word)
    return found_SE or found_NW or found_SW or found_NE

def appear_all_directions(word_board, word):
    '''(list, str) -> (bool)
    Determins if word appears in all directions
    
    >>> appear_all_directions(word_board3, "tea")
    True
    '''
    # looks for the word in either the diagonal or horizontal or vertical 
    # direction
    return appear_hori_vert(word_board, word) or appear_diagonals(word_board, 
                                                                  word)

print("Two pre-made word searches have been made for you above.")
print("Please choose a word search that you would like to use.")
word_board_picked = input("Enter a word search: ")
print("Please enter a lower case word to search for.")
word_picked = input("Enter a word: ")

# while STOP is not entered, checks which word search is chosen and searches
# word in that word search
while(not(word_picked == "STOP")):
    if(word_board_picked == "word_board0"):
        pprint(word_board0)
        print(appear_all_directions(word_board0, word_picked))    
    if(word_board_picked == "word_board1"):
        pprint(word_board1)
        print(appear_all_directions(word_board1, word_picked))
    if(word_board_picked == "word_board2"):
        pprint(word_board2)
        print(appear_all_directions(word_board2, word_picked))
    if(word_board_picked == "word_board3"):
        pprint(word_board3)
        print(appear_all_directions(word_board3, word_picked))
    # asks for next word to search
    word_picked = input("Enter another word, STOP to exit: ")