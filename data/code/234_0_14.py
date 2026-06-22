import matplotlib.pyplot as plt
import numpy as np

def generate_checkerboard(size=8):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    
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
    try:
        checkerboard = generate_checkerboard(8)
        display_checkerboard(checkerboard)
    except ValueError as e:
        print(e)