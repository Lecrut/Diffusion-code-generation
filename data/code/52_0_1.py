def generate_diamond(size):
    lines = []
    for i in range(size):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(size - 2, -1, -1):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    return lines

if __name__ == '__main__':
    size = 5
    diamond_lines = generate_diamond(size)
    for line in diamond_lines:
        print(line)