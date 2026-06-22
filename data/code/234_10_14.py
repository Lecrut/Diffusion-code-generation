import numpy as np

def generate_checkerboard(size=8):
    checkerboard = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                checkerboard[i, j] = 1
    return checkerboard

if __name__ == '__main__':
    checkerboard_pattern = generate_checkerboard()
    print(checkerboard_pattern)