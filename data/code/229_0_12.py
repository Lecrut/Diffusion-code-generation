import matplotlib.pyplot as plt
import numpy as np

def create_square_grid():
    fig, ax = plt.subplots()
    grid = np.zeros((10, 10))
    
    colors = [
        'red', 'green', 'blue', 'cyan', 'magenta',
        'yellow', 'black', 'white', 'gray', 'orange'
    ]
    
    for i in range(10):
        for j in range(10):
            grid[i, j] = colors.index(colors[j % len(colors)])
    
    ax.imshow(grid, cmap='viridis')
    plt.show()

if __name__ == '__main__':
    create_square_grid()