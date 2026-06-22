def print_reverse_number_triangle(row_count):
    for row in range(row_count, 0, -1):
        print(*(list(range(1, row + 1))))

if __name__ == '__main__':
    rows = 5
    print_reverse_number_triangle(rows)