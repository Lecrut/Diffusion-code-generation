def diamond_stars(n):
    for i in range(n):
        spaces = n - 1 - i
        stars = 2 * i + 1
        line = " " * spaces + "*" * stars
        yield line
        if i % 2 == 0:
            yield ""
if __name__ == '__main__':
    n_val = 5
    for line in diamond_stars(n_val):
        print(line)