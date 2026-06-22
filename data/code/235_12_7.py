def print_pyramid_line(n):
    for i in range(1, n + 1):
        line = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        print(spaces + line)

if __name__ == '__main__':
    print_pyramid_line(5)