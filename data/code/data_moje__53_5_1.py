def print_symmetric_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        line = ""
        for num in range(1, i + 1):
            line += str(num)
        print(line)

if __name__ == '__main__':
    print_symmetric_reverse_number_triangle(5)