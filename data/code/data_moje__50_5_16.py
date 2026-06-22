def print_downward_triangle(row_count):
    for row in range(row_count, 0, -1):
        print("* " * row)

if __name__ == "__main__":
    print_downward_triangle(9)