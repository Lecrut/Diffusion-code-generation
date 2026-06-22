def print_diamond(height=7):
    if height % 2 == 0:
        raise ValueError("Height must be an odd number for a symmetric diamond")
    mid = height // 2
    lines = []
    for i in range(mid + 1):
        spaces = ' ' * (mid - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(mid - 1, -1, -1):
        spaces = ' ' * (mid - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(print_diamond(7))