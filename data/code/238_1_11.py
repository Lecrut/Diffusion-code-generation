import matplotlib.pyplot as plt

def create_red_rectangle():
    fig, ax = plt.subplots()
    rect = plt.Rectangle((0, 0), 5, 3, color='red')
    ax.add_patch(rect)
    return fig

if __name__ == '__main__':
    plot_obj = create_red_rectangle()