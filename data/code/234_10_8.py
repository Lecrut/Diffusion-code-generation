import numpy as np

def create_checkerboard(size):
    if size < 1:
        raise ValueError("Size must be at least 1")
    
    checkerboard = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            checkerboard[i, j] = (i + j) % 2
    return checkerboard

if __name__ == '__main__':
    sample_size = 8
    board = create_checkerboard(sample_size)
    print(board)