def print_diamond(height: int=7) -> None:
    mid = height // 2 + 1
    lines = []
    for i in range(1, mid + 1):
        spaces = ' ' * (mid - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(mid - 1, 0, -1):
        spaces = ' ' * (mid - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    print('\n'.join(lines))
if __name__ == '__main__':
    print_diamond(7)