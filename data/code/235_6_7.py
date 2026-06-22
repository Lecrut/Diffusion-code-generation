def print_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        line = spaces + "+" * (2 * i - 1)
        print(line)

if __name__ == '__main__':
    N = 5
    print_pyramid(N)