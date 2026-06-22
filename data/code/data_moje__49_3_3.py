def print_hollow_square(size):
    for i in range(size):
        if i == 0 or i == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

if __name__ == '__main__':
    print_hollow_square(6)