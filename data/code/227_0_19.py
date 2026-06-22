def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

if __name__ == '__main__':
    triangle_rows = {
        'sample': 5
    }
    print_right_triangle(triangle_rows['sample'])