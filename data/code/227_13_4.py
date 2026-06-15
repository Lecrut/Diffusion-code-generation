def diamond_stars(n):
    for i in range(n):
        top = 2 * i + 1
        bottom = 2 * n - 1 - 2 * i
        middle = 2 * n - 1 - (2 * i)
        if i < n // 2:
            line = " " * (n - 1 - i) + "*" * (2 * i + 1)
        else:
            line = " " * i + "*" * (2 * (n - 1 - i) + 1)
        yield line
if __name__ == '__main__':
    size = 5
    for line in diamond_stars(size):
        print(line)