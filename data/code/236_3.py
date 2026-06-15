def print_triangle(n):
    for i in range(1, n + 1):
        print("*" * (2 * i - 1))
if __name__ == '__main__':
    N = 5
    print_triangle(N)