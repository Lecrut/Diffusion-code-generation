def print_diamond_star_pattern(max_width):
    for i in range(max_width):
        spaces = ' ' * (max_width - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    for i in range(max_width - 2, -1, -1):
        spaces = ' ' * (max_width - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond_star_pattern(5)