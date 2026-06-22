def print_right_aligned_triangle(row_count):
    for i in range(1, row_count + 1):
        spaces = " " * (row_count - i)
        stars = "*" * i
        print(spaces + stars)

if __name__ == "__main__":
    sample_row_count = 10
    print_right_aligned_triangle(sample_row_count)