def print_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        line = []
        for num in range(i, 0, -1):
            line.append(str(num))
        print(" ".join(line))

if __name__ == '__main__':
    print_reverse_number_triangle(6)