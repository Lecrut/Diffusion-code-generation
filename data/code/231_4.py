def print_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
if __name__ == '__main__':
    num_rows = 5
    print_triangle(num_rows)