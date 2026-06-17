def print_diamond(n):
    for i in range(n):
        for j in range(2 * n - 1 - 2 * i):
            if j < n - i or j >= n + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__ == '__main__':
    N = 5
    print_diamond(N)