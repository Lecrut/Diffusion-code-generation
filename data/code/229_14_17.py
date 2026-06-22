import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap(matrix):
    sns.heatmap(matrix, cmap='Blues', annot=True, fmt='d')
    plt.show()

if __name__ == '__main__':
    sample_matrix = np.random.randint(0, 101, size=(8, 8))
    plot_heatmap(sample_matrix)