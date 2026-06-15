def diamond_stars(n):
    if n <= 0:
        return
    for i in range(1, n + 1):
        top = " " * (2 * n - 2 * i) + "*" * (2 * i - 1)
        bottom = " " * (2 * n - 2 * i) + "*" * (2 * i - 1)
        if i < n:
            yield top + "\n"
            yield bottom + "\n"
        else:
            yield top + "\n"
if __name__ == '__main__':
    size = 5
    for line in diamond_stars(size):
        print(line, end='')