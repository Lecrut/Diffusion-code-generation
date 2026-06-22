def inverted_triangle_stars(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    for i in range(n, 0, -1):
        stars = 2 * i - 1
        spaces = n - i
        line = " " * spaces + "*" * stars
        yield line

if __name__ == '__main__':
    size = 6
    for line in inverted_triangle_stars(size):
        print(line)