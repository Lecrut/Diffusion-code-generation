def print_star_square(size):
    row = '*' * size
    lines = [row for _ in range(size)]
    print('\n'.join(lines))

if __name__ == '__main__':
    print_star_square(12)