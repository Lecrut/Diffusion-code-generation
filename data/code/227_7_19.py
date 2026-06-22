def validate_input(rows):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer")

def print_inverted_pyramid(rows):
    for i in reversed(range(1, rows + 1)):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    validate_input(5)
    print_inverted_pyramid(5)