def validate_rows(rows):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer")

def print_inverted_pyramid(n):
    validate_rows(n)
    for i in reversed(range(1, n + 1)):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    try:
        print_inverted_pyramid(5)
    except ValueError as e:
        print(e)