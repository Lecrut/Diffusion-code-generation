import matplotlib.pyplot as plt
import numpy as np

def generate_color_grid():
    fig, ax = plt.subplots()
    grid = np.arange(100).reshape(10, 10)
    cax = ax.matshow(grid, cmap='viridis')
    fig.colorbar(cax)
    plt.show()

if __name__ == '__main__':
    generate_color_grid()