import seaborn as sns
import matplotlib.pyplot as plt

def validate_matrix(matrix):
    if not matrix:
        raise ValueError("Matrix is empty")
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("All rows must have the same number of columns")

def plot_heatmap(matrix):
    validate_matrix(matrix)
    sns.heatmap(matrix, annot=True, cmap='YlGnBu')
    plt.show()

if __name__ == '__main__':
    sample_matrix = [
        [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0, 10.0, 11.0, 12.0],
        [13.0, 14.0, 15.0, 16.0, 17.0, 18.0],
        [19.0, 20.0, 21.0, 22.0, 23.0, 24.0],
        [25.0, 26.0, 27.0, 28.0, 29.0, 30.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0]
    ]
    plot_heatmap(sample_matrix)