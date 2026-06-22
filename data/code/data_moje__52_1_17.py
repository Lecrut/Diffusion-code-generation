def print_diamond(height=7):
    if height % 2 == 0:
        height += 1
    middle = height // 2
    lines = []
    for i in range(height):
        spaces = abs(middle - i)
        stars = 2 * (middle - spaces) + 1
        lines.append(' ' * spaces + '*' * stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_diamond(7))