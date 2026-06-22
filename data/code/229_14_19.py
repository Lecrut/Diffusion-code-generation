import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
GRID_SIZE = 8
RANDOM_RANGE = (0, 101)

def generate_random_matrix(size=GRID_SIZE, range=RANDOM_RANGE):
    return np.random.randint(*range, size=(size, size))

def plot_heatmap(matrix):
    sns.heatmap(matrix, annot=True, cmap='YlGnBu')
    plt.show()
if __name__ == '__main__':
    sample_matrix = generate_random_matrix()
    print('Sample 8x8 Matrix:')
    print(sample_matrix)
    plot_heatmap(sample_matrix)