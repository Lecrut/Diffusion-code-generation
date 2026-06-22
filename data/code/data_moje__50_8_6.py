def print_pyramid(base_width):
    if base_width % 2 == 0:
        base_width += 1
    max_stars = base_width
    for i in range(1, max_stars + 1, 2):
        spaces = (max_stars - i) // 2
        stars = '*' * i
        line = ' ' * spaces + stars
        print(line)

if __name__ == '__main__':
    result = print_pyramid(21)