def print_diamond(height: int) -> None:
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    for i in range(height - 1, 0, -1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    sample_height = 5
    print_diamond(sample_height)