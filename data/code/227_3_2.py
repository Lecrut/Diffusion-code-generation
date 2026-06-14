def diamond_generator(n):
    middle = n // 2
    for i in range(n):
        if i <= middle:
            row = "* " * (2 * i + 1)
        else:
            row = "* " * (2 * (n - 1 - i) + 1)
        yield row
if __name__ == '__main__':
    n_value = 5
    diamond = diamond_generator(n_value)
    for row in diamond:
        print(row)