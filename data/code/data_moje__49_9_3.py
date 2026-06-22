def print_star_square(size):
    line = '*' * size
    return '\n'.join([line] * size)

if __name__ == '__main__':
    sample_size = 12
    print(print_star_square(sample_size))