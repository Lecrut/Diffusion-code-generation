import numpy as np
import matplotlib.pyplot as plt
def create_and_visualize_grid():
    N = 10
    grid = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            grid[i, j] = i * 10 + j
    plt.figure(figsize=(8, 8))
    im = plt.imshow(grid, cmap='viridis', origin='upper')
    plt.colorbar(im)
    plt.title('Dynamically Created 10x10 Grid')
    plt.xlabel('Column Index')
    plt.ylabel('Row Index')
    plt.xticks(np.arange(N))
    plt.yticks(np.arange(N))
    plt.grid(False)
    plt.show()
if __name__ == '__main__':
    create_and_visualize_grid()