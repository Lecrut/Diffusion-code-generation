import matplotlib.pyplot as plt

def create_filled_rectangle():
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((0, 0), 5, 3, color='red', fill=True)
    ax.add_patch(rectangle)
    return fig

if __name__ == '__main__':
    plot_object = create_filled_rectangle()
    print(plot_object)