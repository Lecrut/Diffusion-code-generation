import numpy as np
if __name__ == '__main__':
    board_size = 8
    checkerboard = np.zeros((board_size, board_size), dtype=int)
    for i in range(board_size):
        for j in range(board_size):
            if (i + j) % 2 == 0:
                checkerboard[i, j] = 1
            else:
                checkerboard[i, j] = 0
    print(checkerboard)