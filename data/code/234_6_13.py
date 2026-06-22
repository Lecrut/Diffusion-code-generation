import seaborn as sns
import matplotlib.pyplot as plt

class Checkerboard:
    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()

    def generate_board(self):
        return [['A' if (i + j) % 2 == 0 else 'B' for j in range(self.size)] for i in range(self.size)]

    def plot_board(self):
        sns.heatmap(self.board, cmap='Blues', cbar=False)
        plt.show()

if __name__ == '__main__':
    checkerboard = Checkerboard(8)
    checkerboard.plot_board()