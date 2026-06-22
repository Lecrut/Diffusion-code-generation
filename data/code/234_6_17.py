import seaborn as sns
import matplotlib.pyplot as plt

class Checkerboard:
    def __init__(self):
        self.board = [
            ['A' if (i + j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)
        ]

    def plot(self):
        sns.heatmap(self.board, cmap='coolwarm', annot=True, cbar=False)
        plt.show()

if __name__ == '__main__':
    checkerboard = Checkerboard()
    checkerboard.plot()