import seaborn as sns
import matplotlib.pyplot as plt

def generate_checkerboard_data():
    data = [[1 if (i + j) % 2 == 0 else 0 for j in range(8)] for i in range(8)]
    return data

if __name__ == '__main__':
    checkerboard_data = generate_checkerboard_data()
    sns.heatmap(checkerboard_data, cmap='binary', cbar=False)
    plt.show()