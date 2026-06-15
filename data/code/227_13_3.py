def diamond_stars(n):
    for i in range(n):
        stars = 2 * i + 1
        spaces = n - stars
        line = " " * spaces + "*" * stars
        yield line
        if i < n // 2:
            spaces = n - (2 * i + 1)
            line = " " * spaces + "*" * (2 * (n - i) - 1)
            yield line
if __name__ == '__main__':
    size = 5
    for line in diamond_stars(size):
        print(line)