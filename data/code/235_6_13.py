def pyramid_generator(n):
    for i in range(1, n + 1):
        yield " " * (n - i) + "+" * (2 * i - 1)

if __name__ == '__main__':
    N = 5
    pyramid = pyramid_generator(N)
    for line in pyramid:
        print(line)