def print_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        line = ' '.join(str(n) for n in range(1, i + 1))
        print(line)

if __name__ == '__main__':
    row_count = 5
    print_reverse_number_triangle(row_count)