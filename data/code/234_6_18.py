import seaborn as sns
import matplotlib.pyplot as plt

def create_checkerboard_data(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    sample_board = create_checkerboard_data(8)
    sns.heatmap(sample_board, cmap='coolwarm', cbar=False)
    plt.show()