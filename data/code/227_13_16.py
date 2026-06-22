def inverted_triangle_stars(rows):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Number of rows must be a positive integer")
    
    for i in range(rows, 0, -1):
        stars = 2 * i - 1
        spaces = rows - i
        line = " " * spaces + "*" * stars
        yield line

if __name__ == '__main__':
    size = 6
    for line in inverted_triangle_stars(size):
        print(line)