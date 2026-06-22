def diamond(n):
    for i in range(n):
        spaces = n - abs(i + 1)
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    n_value = 5
    diamond(n_value)