def print_diamond_star_pattern(max_width):
    half = max_width // 2 + 1
    for i in range(half):
        spaces = ' ' * (half - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    for i in range(half - 2, -1, -1):
        spaces = ' ' * (half - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond_star_pattern(7)