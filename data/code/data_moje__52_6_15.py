def print_diamond(size):
    if size % 2 == 0:
        size += 1
    upper_half = size // 2 + 1
    for i in range(upper_half):
        spaces = ' ' * (upper_half - 1 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    lower_half = size // 2
    for i in range(lower_half, -1, -1):
        spaces = ' ' * (upper_half - 1 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond(8)