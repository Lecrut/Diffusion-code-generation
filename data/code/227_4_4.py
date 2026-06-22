def print_hollow_square(side_length):
    for i in range(side_length):
        for j in range(side_length):
            if i == 0 or i == side_length - 1 or j == 0 or j == side_length - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

if __name__ == '__main__':
    print_hollow_square(4)