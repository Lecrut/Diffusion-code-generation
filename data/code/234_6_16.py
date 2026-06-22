import seaborn as sns
import matplotlib.pyplot as plt

def generate_checkerboard(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        board.append(row)
    return board

if __name__ == '__main__':
    sample_board = generate_checkerboard(8)
    sns.heatmap(sample_board, cmap='Blues', cbar=False)
    plt.show()