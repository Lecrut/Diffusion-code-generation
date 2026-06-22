def print_diamond(size):
    if size <= 0:
        return
    for i in range(size):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    for i in range(size - 2, -1, -1):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond(5)