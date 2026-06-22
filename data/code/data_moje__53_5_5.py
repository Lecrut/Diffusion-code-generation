def print_symmetric_reverse_number_triangle(rows):
    for i in range(1, rows + 1):
        line = ""
        for j in range(i, rows + 1):
            line += str(j) + " "
        for j in range(rows - 1, i - 1, -1):
            line += str(j) + " "
        print(line.strip())

if __name__ == '__main__':
    print_symmetric_reverse_number_triangle(5)