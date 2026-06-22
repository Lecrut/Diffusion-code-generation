import matplotlib.pyplot as plt

def create_grid():
    fig, ax = plt.subplots()
    colors = [
        'red', 'green', 'blue', 'yellow', 'cyan',
        'magenta', 'black', 'white', 'gray', 'orange'
    ]
    for i in range(10):
        for j in range(10):
            rect = plt.Rectangle((i, j), 1, 1, color=colors[(i + j) % len(colors)])
            ax.add_patch(rect)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    plt.show()

if __name__ == '__main__':
    create_grid()