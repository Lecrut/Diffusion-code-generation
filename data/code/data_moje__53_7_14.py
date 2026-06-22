def print_reverse_number_triangle(rows=6):
    for i in range(rows, 0, -1):
        print(' '.join(map(str, range(1, i + 1))))

if __name__ == '__main__':
    print_reverse_number_triangle(6)