import numpy as np

def generate_checkerboard(size=8):
    board = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                board[i, j] = 1
    return board

if __name__ == '__main__':
    checkerboard = generate_checkerboard(8)
    print(checkerboard)