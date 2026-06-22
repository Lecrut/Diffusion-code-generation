def diamond_generator(n):
    middle = n // 2
    for i in range(n):
        spaces = abs(middle - i)
        stars = n - 2 * spaces
        line = " " * spaces + "*" * stars
        yield line

if __name__ == '__main__':
    n_value = 5
    for row in diamond_generator(n_value):
        print(row)