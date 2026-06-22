import matplotlib.pyplot as plt
import numpy as np

CHECKERBOARD_SIZE = 8

def generate_checkerboard(size=CHECKERBOARD_SIZE):
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
    checkerboard = generate_checkerboard()
    display_checkerboard(checkerboard)