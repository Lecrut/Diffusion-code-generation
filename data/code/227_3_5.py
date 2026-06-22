def diamond_pattern(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "* " * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    n_value = 5
    diamond_pattern(n_value)