def print_symmetric_reverse_triangle(rows):
    for i in range(rows, 0, -1):
        row_numbers = list(range(1, i + 1))
        reverse_part = row_numbers[:-1][::-1]
        full_row = row_numbers + reverse_part
        print(' '.join(str(num) for num in full_row))

if __name__ == '__main__':
    print_symmetric_reverse_triangle(5)