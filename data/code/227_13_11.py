def inverted_triangle_stars(n):
    for i in range(n):
        spaces = n - i - 1
        stars = 2 * i + 1
        line = " " * spaces + "*" * stars
        yield line

if __name__ == '__main__':
    size = 6
    for line in inverted_triangle_stars(size):
        print(line)