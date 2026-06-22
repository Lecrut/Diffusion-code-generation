import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap():
    data = [
        [0.2, 0.3, 0.5, 0.7, 0.8, 0.9],
        [0.1, 0.4, 0.6, 0.8, 0.9, 0.95],
        [0.15, 0.45, 0.65, 0.75, 0.85, 0.95],
        [0.25, 0.55, 0.75, 0.85, 0.95, 0.98],
        [0.35, 0.65, 0.85, 0.95, 0.98, 0.99],
        [0.45, 0.75, 0.95, 0.98, 0.99, 1.0]
    ]
    sns.heatmap(data, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    plot_heatmap()