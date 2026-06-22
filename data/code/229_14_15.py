import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(matrix):
    sns.heatmap(matrix, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    sample_matrix = np.random.randint(0, 101, (8, 8))
    plot_heatmap(sample_matrix)