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
    print(f"Pattern for N={N}:")
    generate_pattern(N)
    print("\n--- Square Pattern ---")
    for i in range(N):
        line = ""
        for j in range(N):
            if i == j:
                line += "*"
            else:
                line += " "
        print(line)