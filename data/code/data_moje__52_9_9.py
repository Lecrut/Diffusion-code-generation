def print_diamond(half_height: int) -> None:
    if half_height <= 0:
        return

    for i in range(1, half_height + 1):
        spaces = " " * (half_height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    for i in range(half_height - 1, 0, -1):
        spaces = " " * (half_height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_diamond(4)