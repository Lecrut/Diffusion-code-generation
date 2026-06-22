def print_star_square(size):
    row = '*' * size
    square = '\n'.join([row] * size)
    return square

if __name__ == '__main__':
    result = print_star_square(12)
    print(result)