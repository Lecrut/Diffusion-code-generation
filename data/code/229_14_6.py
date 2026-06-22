import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap():
    data = np.random.randint(0, 101, size=(8, 8))
    sns.heatmap(data, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    plot_heatmap()