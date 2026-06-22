def print_hollow_square(size):
    if size <= 0:
        return
    for row in range(size):
        if row == 0 or row == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

if __name__ == '__main__':
    print_hollow_square(6)