def generate_diamond(height=7):
    half = height // 2 + 1
    lines = []
    for i in range(1, half + 1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(half - 1, 0, -1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return lines

if __name__ == '__main__':
    result = generate_diamond(7)
    for line in result:
        print(line)