import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap(matrix):
    sns.heatmap(matrix, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    sample_matrix = np.random.randint(0, 100, size=(8, 8))
    plot_heatmap(sample_matrix)