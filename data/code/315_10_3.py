import sys
def generate_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__ == '__main__':
    N = 5
    print(f"Pattern for N = {N}:")
    generate_pattern(N)
    print("\n--- Square Pattern (Filled) ---")
    for i in range(N):
        for j in range(N):
            print("*", end=" ")
        print()
    print("\n--- Triangle Pattern (Right-angled) ---")
    for i in range(1, N + 1):
        for j in range(i):
            print("*", end="")
        print()