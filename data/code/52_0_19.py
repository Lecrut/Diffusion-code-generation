def generate_diamond_pattern(size):
    lines = []
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(size - 1, 0, -1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return lines
if __name__ == '__main__':
    size = 5
    diamond_lines = generate_diamond_pattern(size)
    for line in diamond_lines:
        print(line)