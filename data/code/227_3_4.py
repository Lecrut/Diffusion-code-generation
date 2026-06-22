def print_diamond_star_pattern(max_width):
    for i in range(1, max_width + 1):
        spaces = ' ' * (max_width - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

    for i in range(max_width - 1, 0, -1):
        spaces = ' ' * (max_width - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond_star_pattern(5)