import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class GridPlotter:
    def __init__(self, size=8):
        self.size = size
        self.data = np.random.randint(0, 101, size=(size, size))

    @staticmethod
    def create_heatmap(data):
        sns.heatmap(data, annot=True, cmap='YlGnBu', fmt='d')
        plt.show()

if __name__ == '__main__':
    plotter = GridPlotter()
    GridPlotter.create_heatmap(plotter.data)