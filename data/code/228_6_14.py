def print_triangle(level, max_level):
    if level > max_level:
        return
    spaces = ' ' * (max_level - level)
    stars = '*' * (2 * level - 1)
    print(spaces + stars)
    print_triangle(level + 1, max_level)

if __name__ == '__main__':
    height = 4
    print_triangle(1, height)