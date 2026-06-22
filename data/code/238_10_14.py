BOX_WIDTH = 5
BOX_HEIGHT = 3

def print_box(width=BOX_WIDTH, height=BOX_HEIGHT):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

if __name__ == '__main__':
    print_box()