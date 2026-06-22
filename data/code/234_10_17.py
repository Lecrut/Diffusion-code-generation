import numpy as np

CHECKERBOARD_SIZE = 8
ZERO = 0
ONE = 1

def generate_checkerboard(size=CHECKERBOARD_SIZE):
    board = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                board[i, j] = ONE
    return board

if __name__ == '__main__':
    checkerboard = generate_checkerboard()
    print(checkerboard)