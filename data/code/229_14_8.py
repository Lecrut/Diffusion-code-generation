import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_random_heatmap(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer.")
    
    data = np.random.randint(0, 100, (size, size))
    sns.heatmap(data, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    try:
        plot_random_heatmap(8)
    except ValueError as e:
        print(e)