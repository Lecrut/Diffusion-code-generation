def print_diamond_pattern(half_height: int) -> None:
    for i in range(half_height):
        spaces = ' ' * (half_height - 1 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    for i in range(half_height - 2, -1, -1):
        spaces = ' ' * (half_height - 1 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond_pattern(4)