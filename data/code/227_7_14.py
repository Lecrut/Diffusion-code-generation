def print_inverted_pyramid_star_pattern(rows):
    for i in reversed(range(1, rows + 1)):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    print_inverted_pyramid_star_pattern(5)