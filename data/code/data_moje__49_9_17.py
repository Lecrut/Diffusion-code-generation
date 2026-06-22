def print_square_pattern(size):
    line = '*' * size
    return '\n'.join([line] * size)

if __name__ == '__main__':
    sample_size = 12
    print(print_square_pattern(sample_size))