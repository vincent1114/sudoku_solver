BOARD = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
        if solve(board):
            return True
        board[row][col] = 0
    return False
        
def print_board(board):
    for i in range (len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range (len(board[i])):
            if j % 3 == 0 and j != 0: 
                print(" | ", end = "")
            print(str(board[i][j]) + " ", end = "")
        print("")
def valid(board, num, pos):
    row = pos[0]
    col = pos[1]
    # check rows
    if num in board[row]:
        return False
    # check columns
    for i in range(board):
        if board[row][i] == num:
            return False
    # check squares
    row_st = row // 3
    col_st = col // 3
    for i in range(row_st * 3, row_st *3 + 3):
        for j in range(col_st * 3, col_st*3 + 3):
            if board[i][j] == num:
                return False

    return True
def find_empty(board):
    for i in range (len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j) #row, col
    return None
if __name__ == "__main__":
    print_board(BOARD)
    solve(BOARD)
    print_board(BOARD)
    