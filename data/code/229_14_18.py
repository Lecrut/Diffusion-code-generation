import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class GridPlotter:
    SIZE = 8
    MIN_VALUE = 0
    MAX_VALUE = 100
    
    @staticmethod
    def generate_data():
        return np.random.randint(GridPlotter.MIN_VALUE, GridPlotter.MAX_VALUE + 1, (GridPlotter.SIZE, GridPlotter.SIZE))
    
    @staticmethod
    def plot_heatmap(data):
        sns.heatmap(data, annot=True, cmap='YlGnBu')
        plt.show()

if __name__ == '__main__':
    data = GridPlotter.generate_data()
    GridPlotter.plot_heatmap(data)