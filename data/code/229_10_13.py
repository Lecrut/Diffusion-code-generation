import matplotlib.pyplot as plt
import numpy as np

def generate_color_grid(size):
    grid = np.linspace(0, 1, size * size).reshape((size, size))
    colors = plt.cm.viridis(grid)
    return colors

if __name__ == '__main__':
    grid_size = 10
    color_grid = generate_color_grid(grid_size)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(color_grid, interpolation='nearest')
    ax.axis('off')
    plt.show()