def print_inverted_pyramid(rows):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Input must be a positive integer")

    for i in range(rows, 0, -1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    try:
        print_inverted_pyramid(5)
    except ValueError as e:
        print(e)