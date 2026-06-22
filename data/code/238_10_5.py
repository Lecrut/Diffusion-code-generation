def print_box(width=5, height=3):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

if __name__ == '__main__':
    print_box()