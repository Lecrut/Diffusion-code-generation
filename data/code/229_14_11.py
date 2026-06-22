import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

GRID_SIZE = 8
RANDOM_SEED = 42

def generate_random_matrix(size, seed):
    np.random.seed(seed)
    return np.random.randint(0, 101, (size, size))

def plot_heatmap(matrix):
    sns.heatmap(matrix, annot=True, cmap="YlGnBu")
    plt.show()

if __name__ == '__main__':
    sample_matrix = generate_random_matrix(GRID_SIZE, RANDOM_SEED)
    plot_heatmap(sample_matrix)