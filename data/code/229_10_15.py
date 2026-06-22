import matplotlib.pyplot as plt
import numpy as np

def generate_square_grid(size):
    grid = np.linspace(0, 1, size)
    colors = plt.cm.viridis(grid)
    return colors.reshape((size, size))

if __name__ == '__main__':
    grid_size = 10
    color_grid = generate_square_grid(grid_size)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(color_grid, interpolation='nearest')
    ax.axis('off')
    plt.show()