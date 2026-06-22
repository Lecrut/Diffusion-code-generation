def print_downward_triangle(row_count):
    for current_row in range(row_count, 0, -1):
        print('* ' * current_row)

if __name__ == '__main__':
    print_downward_triangle(9)