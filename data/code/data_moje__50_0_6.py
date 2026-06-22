def print_right_aligned_triangle(row_count):
    for i in range(1, row_count + 1):
        line = '*' * i
        print(line.rjust(row_count))

if __name__ == '__main__':
    result = print_right_aligned_triangle(10)