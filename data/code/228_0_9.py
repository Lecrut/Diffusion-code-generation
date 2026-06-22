def validate_input(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Input must be a positive integer')

def print_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
if __name__ == '__main__':
    try:
        height = 5
        validate_input(height)
        print_triangle(height)
    except ValueError as e:
        print(e)