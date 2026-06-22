def print_symmetric_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        line = []
        for j in range(1, i + 1):
            line.append(str(j))
        full_line = ''.join(line + list(reversed(line[:-1])))
        print(full_line)

if __name__ == '__main__':
    print_symmetric_reverse_number_triangle(5)