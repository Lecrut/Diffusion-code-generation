import matplotlib.pyplot as plt
import numpy as np

def generate_checkerboard(size=8):
    checkerboard = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                checkerboard[i, j] = 1
    return checkerboard

def display_checkerboard(checkerboard):
    plt.imshow(checkerboard, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    sample_size = 8
    board = generate_checkerboard(sample_size)
    display_checkerboard(board)