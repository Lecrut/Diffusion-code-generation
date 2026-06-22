import matplotlib.pyplot as plt

def create_grid():
    fig, ax = plt.subplots()
    colors = [
        'red', 'green', 'blue', 'yellow', 'purple',
        'orange', 'pink', 'gray', 'cyan', 'magenta'
    ]
    for i in range(10):
        for j in range(10):
            color = colors[(i + j) % len(colors)]
            ax.add_patch(plt.Rectangle((j, 9 - i), 1, 1, color=color))
    plt.xlim(-0.5, 10.5)
    plt.ylim(-0.5, 10.5)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    create_grid()