import matplotlib.pyplot as plt

def generate_checkerboard(size=8):
    if size < 1:
        raise ValueError("Size must be greater than 0")
    checkerboard = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        checkerboard.append(row)
    return checkerboard

def display_checkerboard(checkerboard):
    plt.imshow(checkerboard, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    try:
        checkerboard = generate_checkerboard()
        display_checkerboard(checkerboard)
    except ValueError as e:
        print(e)