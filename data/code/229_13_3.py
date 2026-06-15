import numpy as np
import matplotlib.pyplot as plt
def create_and_visualize_grid():
    size = 10
    grid = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            grid[i, j] = i * 10 + j
    fig, ax = plt.subplots()
    im = ax.imshow(grid)
    ax.set_title("Dynamically Created 10x10 Grid")
    ax.set_xticks(np.arange(size))
    ax.set_yticks(np.arange(size))
    plt.show()
if __name__ == '__main__':
    create_and_visualize_grid()