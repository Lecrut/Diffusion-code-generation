def print_square(N):
    for i in range(N):
        for j in range(N):
            print("*", end="")
            if j < N - 1:
                print(" ", end="")
            print()
if __name__ == '__main__':
    print("--- Square for N=3 ---")
    print_square(3)
    print("\n--- Square for N=5 ---")
    print_square(5)