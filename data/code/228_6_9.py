def print_pyramid(height):
    if not isinstance(height, int) or height < 1:
        raise ValueError("Height must be a positive integer")

    def build_line(n, spaces):
        return " " * spaces + "*" * (2 * n - 1)

    for i in range(1, height + 1):
        print(build_line(i, height - i))

if __name__ == '__main__':
    try:
        print_pyramid(5)
    except ValueError as e:
        print(e)