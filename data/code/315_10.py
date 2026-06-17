import time
def generate_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
def generate_square(n):
    for i in range(n):
        row = ""
        for j in range(n):
            row += "* "
        print(row)
def generate_triangle(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
if __name__ == '__main__':
    N = 5
    print("--- Square Pattern ---")
    generate_square(N)
    print("\n--- Triangle Pattern ---")
    generate_triangle(N)
    print("\n--- Diagonal/Nested Loop Pattern (Square with spaces) ---")
    generate_pattern(N)