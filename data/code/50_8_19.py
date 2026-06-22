def print_pyramid():
    width = 21
    lines = []
    for i in range(1, width + 1, 2):
        spaces = ' ' * ((width - i) // 2)
        stars = '*' * i
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_pyramid())