import sys
def generate_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
if __name__ == '__main__':
    N = 5
    print(f"Pattern for N = {N}:")
    generate_pattern(N)
    print("\n--- Square Pattern (Diagonal emphasis) ---")
    for i in range(N):
        row = ""
        for j in range(N):
            if i == j:
                row += "*"
            else:
                row += " "
        print(row)
    print("\n--- Triangle Pattern (Right-angled) ---")
    for i in range(1, N + 1):
        row = ""
        for j in range(i):
            row += "*"
        print(row)