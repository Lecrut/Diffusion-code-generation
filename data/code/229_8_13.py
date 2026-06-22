import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap():
    data = [
        [0.5, 0.3, 0.2, 0.8, 0.7, 0.6],
        [0.4, 0.9, 0.1, 0.5, 0.3, 0.2],
        [0.6, 0.7, 0.8, 0.9, 0.5, 0.4],
        [0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
        [0.8, 0.9, 0.1, 0.2, 0.3, 0.4],
        [0.5, 0.6, 0.7, 0.8, 0.9, 0.1]
    ]
    sns.set()
    heatmap = sns.heatmap(data, annot=True, cmap='YlGnBu', fmt=".2f")
    plt.title("Intensity Heatmap")
    plt.show()

if __name__ == '__main__':
    plot_heatmap()