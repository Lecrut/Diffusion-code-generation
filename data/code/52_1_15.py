def print_diamond(height=7):
    if height % 2 == 0:
        height += 1
    middle = height // 2 + 1
    lines = []
    for i in range(1, middle + 1):
        spaces = ' ' * (middle - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(middle - 1, 0, -1):
        spaces = ' ' * (middle - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_diamond(7))