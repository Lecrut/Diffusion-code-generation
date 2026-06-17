def print_right_triangle(rows):
    for i in range(rows):
        print('*' * (i + 1))
if __name__ == '__main__':
    num_rows = 5
    print_right_triangle(num_rows)