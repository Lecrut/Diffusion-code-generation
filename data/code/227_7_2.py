def print_inverted_pyramid(n):
    for i in reversed(range(1, n + 1)):
        print(' ' * (n - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    print_inverted_pyramid(5)