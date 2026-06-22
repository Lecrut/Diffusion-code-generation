def create_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        yield spaces + stars

if __name__ == '__main__':
    N = 5
    pyramid = create_pyramid(N)
    for line in pyramid:
        print(line)