import seaborn as sns
import matplotlib.pyplot as plt

def create_checkerboard_data(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    return [[(i + j) % 2 == 0 for j in range(n)] for i in range(n)]

if __name__ == '__main__':
    sample_board = create_checkerboard_data(8)
    sns.heatmap(sample_board, cmap='Greens', cbar=False)
    plt.show()