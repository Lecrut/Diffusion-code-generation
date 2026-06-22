import matplotlib.pyplot as plt

def create_grid():
    fig, ax = plt.subplots()
    colors = [
        'red', 'green', 'blue', 'yellow', 'cyan',
        'magenta', 'white', 'black', 'gray', 'orange'
    ]
    grid = [[colors[i % len(colors)] for i in range(10)] for _ in range(10)]
    
    for i in range(10):
        for j in range(10):
            ax.add_patch(plt.Rectangle((i, 9-j), 1, 1, color=grid[i][j]))
    
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-0.5, 9.5)
    ax.axis('off')
    plt.show()

if __name__ == '__main__':
    create_grid()