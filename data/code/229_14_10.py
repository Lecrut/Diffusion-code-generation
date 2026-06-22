import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class GridPlotter:
    SIZE = 8
    MIN_VALUE = 0
    MAX_VALUE = 100
    
    @staticmethod
    def generate_data(size, min_val, max_val):
        return np.random.randint(min_val, max_val + 1, (size, size))
    
    @staticmethod
    def plot_heatmap(data):
        sns.heatmap(data, cmap='YlGnBu')
        plt.show()

if __name__ == '__main__':
    data = GridPlotter.generate_data(GridPlotter.SIZE, GridPlotter.MIN_VALUE, GridPlotter.MAX_VALUE)
    GridPlotter.plot_heatmap(data)