import numpy as np
import matplotlib.pyplot as plt
def create_and_visualize_grid():
    size = 10
    grid = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            grid[i, j] = i * 10 + j
    plt.figure(figsize=(8, 8))
    im = plt.imshow(grid, cmap='viridis', origin='upper')
    plt.colorbar(im)
    plt.title('Dynamically Created 10x10 Grid')
    plt.xlabel('Column Index')
    plt.ylabel('Row Index')
    plt.xticks(np.arange(size))
    plt.yticks(np.arange(size))
    plt.grid(False)
    plt.show()
if __name__ == '__main__':
    create_and_visualize_grid()