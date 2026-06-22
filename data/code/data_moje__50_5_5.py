def print_downward_triangle(num_rows):
    for i in range(num_rows, 0, -1):
        print('*' * i)
if __name__ == '__main__':
    row_count = 9
    print_downward_triangle(row_count)