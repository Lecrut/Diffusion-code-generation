import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_random_heatmap(size=8):
    data = np.random.randint(0, 100, size=(size, size))
    sns.heatmap(data, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    plot_random_heatmap()