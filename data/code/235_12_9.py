def print_pyramid_line(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(f"{spaces}{stars}")

if __name__ == '__main__':
    print_pyramid_line(5)