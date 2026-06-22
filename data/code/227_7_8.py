def print_inverted_pyramid(rows):
    for i in reversed(range(1, rows + 1)):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_inverted_pyramid(5)