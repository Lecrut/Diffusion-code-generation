def diamond_stars(n):
    for i in range(n):
        spaces = " " * (n - 1 - i)
        stars = "*" * (2 * i + 1)
        line = spaces + stars + spaces
        yield line
if __name__ == '__main__':
    size = 5
    for line in diamond_stars(size):
        print(line)