def print_diamond(height):
    rows = []
    for i in range(height):
        spaces = ' ' * (height - 1 - abs(height // 2 - i))
        stars = '*' * (1 + 2 * abs(height // 2 - i))
        rows.append(spaces + stars)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(print_diamond(5))