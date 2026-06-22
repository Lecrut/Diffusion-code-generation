import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(data):
    sns.heatmap(data, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    sample_data = [
        [0.25, 0.5, 0.75, 1.0],
        [1.25, 1.5, 1.75, 2.0],
        [2.25, 2.5, 2.75, 3.0],
        [3.25, 3.5, 3.75, 4.0]
    ]
    plot_heatmap(sample_data)