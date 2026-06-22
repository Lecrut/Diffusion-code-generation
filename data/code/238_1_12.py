import matplotlib.pyplot as plt

def create_filled_rectangle():
    fig, ax = plt.subplots()
    rect = plt.Rectangle((0, 0), 5, 3, color='red', fill=True)
    ax.add_patch(rect)
    return fig

if __name__ == '__main__':
    plot_obj = create_filled_rectangle()