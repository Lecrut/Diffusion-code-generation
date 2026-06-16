def print_diamond(n):
    for i in range(n + 1):
        stars = 2 * i + 1
        spaces = n - i
        print(" " * spaces + "*" * stars)
        if i < n:
            print()
if __name__ == '__main__':
    N = 5
    print_diamond(N)