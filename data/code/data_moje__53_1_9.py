def print_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        line = ''.join(str(j) for j in range(1, i + 1))
        print(line.rjust(rows * 2 - 1))

if __name__ == '__main__':
    print_reverse_number_triangle(4)