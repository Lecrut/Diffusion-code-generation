def print_right_aligned_triangle(row_count=10):
    for i in range(1, row_count + 1):
        line = ' ' * (row_count - i) + '*' * i
        print(line)
if __name__ == '__main__':
    print_right_aligned_triangle(10)