def print_inverted_triangle_star_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    for i in range(n, 0, -1):
        stars = 2 * i - 1
        spaces = n - stars
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    print_inverted_triangle_star_pattern(6)