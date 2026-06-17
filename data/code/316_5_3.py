def print_diamond(N):
    for i in range(N):
        for j in range(2 * N - 1 - 2 * i):
            if j < N - i or j >= N + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__ == '__main__':
    N = 5
    print_diamond(N)