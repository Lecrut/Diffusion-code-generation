def print_right_angle_inverted_triangle(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    for i in range(n, 0, -1):
        stars = "*" * i
        spaces = " " * (n - i)
        line = spaces + stars
        print(line)

if __name__ == '__main__':
    size = 6
    print_right_angle_inverted_triangle(size)