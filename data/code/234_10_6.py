import numpy as np

def generate_checkerboard(size=8):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
    board = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 1:
                board[i, j] = 1
    return board

if __name__ == '__main__':
    checkerboard = generate_checkerboard()
    print(checkerboard)