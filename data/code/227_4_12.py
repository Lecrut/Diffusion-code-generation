def print_hollow_square(side_length):
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            print('*' * side_length)
        else:
            print('*' + ' ' * (side_length - 2) + '*')

if __name__ == '__main__':
    print_hollow_square(4)