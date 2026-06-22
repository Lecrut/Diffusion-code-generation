def print_diamond(half_height):
    if half_height <= 0:
        return

    for row in range(1, half_height + 1):
        spaces = half_height - row
        stars = 2 * row - 1
        print(" " * spaces + "*" * stars)

    for row in range(half_height - 1, 0, -1):
        spaces = half_height - row
        stars = 2 * row - 1
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    print_diamond(4)