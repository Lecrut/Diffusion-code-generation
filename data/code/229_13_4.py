import numpy as np
import matplotlib.pyplot as plt
def create_and_visualize_grid():
    N = 10
    grid = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            grid[i, j] = i * 10 + j
    fig, ax = plt.subplots()
    im = ax.imshow(grid)
    ax.set_title("Dynamically Created 10x10 Grid")
    ax.set_xticks(np.arange(N))
    ax.set_yticks(np.arange(N))
    plt.show()
if __name__ == '__main__':
    create_and_visualize_grid()