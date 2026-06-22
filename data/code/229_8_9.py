import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap():
    data = [
        [0.5, 0.3, 0.8, 0.2, 0.7, 0.6],
        [0.4, 0.9, 0.1, 0.5, 0.3, 0.8],
        [0.7, 0.2, 0.6, 0.4, 0.9, 0.3],
        [0.2, 0.8, 0.5, 0.1, 0.7, 0.4],
        [0.6, 0.3, 0.9, 0.8, 0.2, 0.5],
        [0.9, 0.7, 0.4, 0.3, 0.1, 0.6]
    ]
    sns.heatmap(data, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    plot_heatmap()