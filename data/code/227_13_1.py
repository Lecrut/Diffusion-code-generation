def diamond_stars(n):
    for i in range(n):
        top = 2 * n - 1 - 2 * i
        middle = 2 * i + 1
        stars = " " * i + "*" * (top - 2 * i) + " " * i
        yield stars
if __name__ == '__main__':
    size = 5
    for line in diamond_stars(size):
        print(line)