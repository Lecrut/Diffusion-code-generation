def print_square(N):
    for i in range(N):
        for j in range(N):
            print("*", end="")
            if j < N - 1:
                print(" ", end="")
            print()
if __name__ == '__main__':
    print("--- Example 1 (N=3) ---")
    print_square(3)
    print("\n--- Example 2 (N=5) ---")
    print_square(5)