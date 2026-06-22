import matplotlib.pyplot as plt

def create_grid():
    fig, ax = plt.subplots()
    colors = [
        'red', 'blue', 'green', 'yellow', 'purple',
        'orange', 'pink', 'gray', 'brown', 'cyan'
    ]
    for i in range(10):
        for j in range(10):
            ax.add_patch(plt.Rectangle((i, j), 1, 1, color=colors[(i + j) % len(colors)]))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    plt.show()

if __name__ == '__main__':
    create_grid()