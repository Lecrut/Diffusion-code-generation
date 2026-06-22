def print_diamond_star_pattern(max_width):
    for i in range(1, max_width + 1):
        print(' ' * (max_width - i) + '*' * (2 * i - 1))
    for i in range(max_width - 1, 0, -1):
        print(' ' * (max_width - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    print_diamond_star_pattern(5)