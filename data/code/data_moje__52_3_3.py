def print_diamond(n):
    top_half = n
    for i in range(1, top_half + 1):
        spaces = ' ' * (top_half - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    bottom_half = n - 1
    for i in range(bottom_half, 0, -1):
        spaces = ' ' * (top_half - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond(6)