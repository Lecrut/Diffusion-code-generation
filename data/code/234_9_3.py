import numpy as np
def print_checkerboard(size):
    board = np.zeros((size, size), dtype=str)
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                board[i, j] = ' '
            else:
                board[i, j] = 'X'
    for row in board:
        print(" ".join(row))
if __name__ == '__main__':
    board_size = 5
    print_checkerboard(board_size)