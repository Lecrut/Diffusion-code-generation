def print_right_aligned_triangle(row_count):
    for row in range(1, row_count + 1):
        spaces = row_count - row
        asterisks = row * "*"
        print(" " * spaces + asterisks)

if __name__ == "__main__":
    print_right_aligned_triangle(10)