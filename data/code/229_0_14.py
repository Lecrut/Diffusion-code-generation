import matplotlib.pyplot as plt

class GridGenerator:
    COLORS = [
        'red', 'green', 'blue', 'yellow', 'cyan',
        'magenta', 'black', 'white', 'gray', 'orange'
    ]

    @staticmethod
    def generate_grid():
        fig, ax = plt.subplots()
        for i in range(10):
            for j in range(10):
                color = GridGenerator.COLORS[(i + j) % len(GridGenerator.COLORS)]
                ax.add_patch(plt.Rectangle((j, 9 - i), 1, 1, color=color))
        ax.set_xlim(-0.5, 10.5)
        ax.set_ylim(-0.5, 10.5)
        ax.axis('off')
        plt.show()

if __name__ == '__main__':
    GridGenerator.generate_grid()