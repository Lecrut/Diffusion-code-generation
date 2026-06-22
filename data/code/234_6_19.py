import seaborn as sns
import matplotlib.pyplot as plt

def generate_checkerboard_data():
    return [[(i + j) % 2 for j in range(8)] for i in range(8)]

if __name__ == '__main__':
    data = generate_checkerboard_data()
    sns.heatmap(data, cmap='coolwarm', cbar=False)
    plt.show()