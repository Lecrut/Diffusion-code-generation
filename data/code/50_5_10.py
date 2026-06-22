def print_downward_triangle(row_count):
    for i in range(row_count, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    rows = 9
    print_downward_triangle(rows)