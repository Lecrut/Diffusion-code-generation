import numpy as np
if __name__ == '__main__':
    board_size = 5
    board = np.zeros((board_size, board_size), dtype=int)
    for i in range(board_size):
        for j in range(board_size):
            if (i + j) % 2 == 0:
                board[i, j] = 1
            else:
                board[i, j] = 0
    for row in board:
        print(" ".join(map(str, row)))