import seaborn as sns
import matplotlib.pyplot as plt

def plot_checkerboard():
    data = [[(i + j) % 2 for j in range(8)] for i in range(8)]
    sns.heatmap(data, cmap='binary', cbar=False)
    plt.show()

if __name__ == '__main__':
    plot_checkerboard()