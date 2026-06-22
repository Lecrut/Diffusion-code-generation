import seaborn as sns
import matplotlib.pyplot as plt

def create_checkerboard():
    data = {
        (i, j): ('A' if (i + j) % 2 == 0 else 'B') for i in range(8) for j in range(8)
    }
    return data

if __name__ == '__main__':
    checkerboard_data = create_checkerboard()
    sns.heatmap(pd.DataFrame(checkerboard_data), annot=True, fmt='s', cmap=['white', 'black'])
    plt.show()