def diamond_stars(n):
    for i in range(n):
        top = 2 * i + 1
        bottom = 2 * n - 1 - 2 * i
        middle = 2 * n - 1 - (top - 1)
        if i < n // 2:
            line = "*" * (2 * i + 1)
        else:
            line = "*" * (2 * (n - 1 - i) + 1)
        if i == n // 2 - 1:
            yield line
        elif i > n // 2 - 1 and i < n:
            yield line
def diamond_stars_optimized(n):
    if n <= 0:
        return
    for i in range(n):
        if i < n / 2:
            spaces = n - 1 - i
            stars = 2 * i + 1
            line = " " * spaces + "*" * (2 * stars - 1)
        else:
            spaces = i
            stars = 2 * (n - 1 - i) + 1
            line = " " * spaces + "*" * stars
        yield line
if __name__ == '__main__':
    test_n = 5
    print(f"Diamond pattern for n={test_n}:")
    for line in diamond_stars_optimized(test_n):
        print(line)