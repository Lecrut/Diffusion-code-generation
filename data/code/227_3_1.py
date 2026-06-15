def diamond_generator(n):
    middle = n // 2
    for i in range(n):
        if i <= middle:
            spaces = middle - i
            stars = 2 * i + 1
            line = " " * spaces + "*" * stars
        else:
            spaces = i - middle
            stars = 2 * (n - i) + 1
            line = " " * spaces + "*" * stars
        yield line
if __name__ == '__main__':
    n_val = 5
    for row in diamond_generator(n_val):
        print(row)