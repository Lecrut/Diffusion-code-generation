def print_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        line = ""
        for j in range(1, i + 1):
            line += str(j) + " "
        print(line.rstrip())

if __name__ == '__main__':
    print_reverse_number_triangle(6)