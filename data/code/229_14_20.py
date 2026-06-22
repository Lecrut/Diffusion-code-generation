import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_random_heatmap(size):
    data = np.random.randint(0, 100, (size, size))
    sns.heatmap(data, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    sample_size = 8
    print(f"--- Random Heatmap of Size {sample_size}x{sample_size} ---")
    plot_random_heatmap(sample_size)