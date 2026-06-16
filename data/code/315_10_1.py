import time
def generate_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
def generate_square(n):
    for i in range(n):
        row = ""
        for j in range(n):
            row += "* "
        print(row)
def generate_right_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
if __name__ == '__main__':
    N = 5
    print("--- Square Pattern (N={}) ---".format(N))
    generate_square(N)
    print("\n--- Right Triangle Pattern (N={}) ---".format(N))
    generate_right_triangle(N)
    print("\n--- Diagonal/Square-like Pattern (N={}) ---".format(N))
    generate_pattern(N)