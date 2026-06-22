import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap():
    data = np.random.randint(0, 100, size=(8, 8))
    sns.heatmap(data)
    plt.show()

if __name__ == '__main__':
    plot_heatmap()