def print_diamond(height=7):
    if height % 2 == 0:
        height += 1
    mid = height // 2
    lines = []
    for i in range(height):
        spaces = abs(mid - i)
        stars = 2 * (mid - spaces) + 1
        lines.append(' ' * spaces + '*' * stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_diamond(7))