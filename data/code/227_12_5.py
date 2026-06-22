def print_diamond_star_pattern():
    max_width = 7
    half_height = (max_width + 1) // 2
    for i in range(half_height):
        spaces = ' ' * (half_height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    for i in range(half_height - 2, -1, -1):
        spaces = ' ' * (half_height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
if __name__ == '__main__':
    print_diamond_star_pattern()