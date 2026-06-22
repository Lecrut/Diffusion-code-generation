def print_inverted_pyramid(base_width):
    for i in range(base_width // 2, -1, -1):
        spaces = ' ' * (base_width - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_inverted_pyramid(9)