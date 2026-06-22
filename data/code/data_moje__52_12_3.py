def print_diamond(radius):
    if radius < 1:
        return
    top_lines = []
    for i in range(radius):
        spaces = ' ' * (radius - 1 - i)
        stars = '*' * (2 * i + 1)
        top_lines.append(spaces + stars)
    bottom_lines = []
    for i in range(radius - 2, -1, -1):
        spaces = ' ' * (radius - 1 - i)
        stars = '*' * (2 * i + 1)
        bottom_lines.append(spaces + stars)
    result = top_lines + bottom_lines
    for line in result:
        print(line)

if __name__ == '__main__':
    print_diamond(5)