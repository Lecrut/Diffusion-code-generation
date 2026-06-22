def pyramid_pattern(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        plus_signs = "+" * (2 * i - 1)
        yield spaces + plus_signs

if __name__ == '__main__':
    N = 5
    pyramid = pyramid_pattern(N)
    for line in pyramid:
        print(line)