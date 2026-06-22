import matplotlib.pyplot as plt
import numpy as np

def generate_checkerboard():
    board = np.zeros((8, 8), dtype=int)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                board[i, j] = 1
    return board

if __name__ == '__main__':
    checkerboard = generate_checkerboard()
    plt.imshow(checkerboard, cmap='gray')
    plt.axis('off')
    plt.show()