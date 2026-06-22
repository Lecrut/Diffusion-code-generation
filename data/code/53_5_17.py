def print_symmetric_reverse_triangle(rows):
    for i in range(rows, 0, -1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        for j in range(i - 1, 0, -1):
            line += str(j)
        print(line)

if __name__ == '__main__':
    print_symmetric_reverse_triangle(5)