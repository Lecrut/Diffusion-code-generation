import matplotlib.pyplot as plt
import numpy as np

def create_checkerboard():
    checkerboard = np.zeros((8, 8), dtype=int)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                checkerboard[i, j] = 1
    return checkerboard

def display_checkerboard(checkerboard):
    plt.imshow(checkerboard, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    checkerboard = create_checkerboard()
    display_checkerboard(checkerboard)