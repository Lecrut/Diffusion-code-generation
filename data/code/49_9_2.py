def print_star_square(size):
    line = '*' * size
    print('\n'.join([line] * size))

if __name__ == '__main__':
    print_star_square(12)