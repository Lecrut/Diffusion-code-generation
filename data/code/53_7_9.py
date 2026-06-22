def print_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        line = " ".join(str(num) for num in range(1, i + 1))
        print(line)

if __name__ == '__main__':
    print_reverse_number_triangle(6)