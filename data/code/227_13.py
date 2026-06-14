def diamond_stars(n):
    for i in range(n):
        stars = 2 * i + 1
        spaces = n - stars
        line = " " * spaces + "*" * stars
        yield line
        if i < n // 2:
            middle_spaces = (n - stars) // 2
            padding = " " * middle_spaces
            yield padding + "*" * (stars - 2) + " " * (stars - 1) + "*" * (stars - 2)
if __name__ == '__main__':
    size = 5
    for line in diamond_stars(size):
        print(line)