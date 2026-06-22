def print_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

if __name__ == '__main__':
    print_reverse_number_triangle(5)