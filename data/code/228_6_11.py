def validate_input(base, height):
    if not isinstance(base, int) or base <= 0:
        raise ValueError("Base must be a positive integer")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")

def print_triangle_line(n, spaces):
    line = ' ' * spaces + '*' * (2 * n - 1)
    print(line)

def construct_pyramid(base, height, current_height=1):
    validate_input(base, height)
    if current_height > height:
        return
    print_triangle_line(current_height, base - current_height)
    construct_pyramid(base, height, current_height + 1)

if __name__ == '__main__':
    base = 5
    height = 4
    construct_pyramid(base, height)