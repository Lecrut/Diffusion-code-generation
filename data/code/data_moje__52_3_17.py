def print_diamond(n):
    for i in range(n):
        spaces = ' ' * (n - 1 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - 1 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond(6)