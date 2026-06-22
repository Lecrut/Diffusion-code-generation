def print_reverse_number_triangle(height):
    for i in range(height, 0, -1):
        row = ''.join(str(n) for n in range(i, 0, -1))
        print(row)

if __name__ == '__main__':
    print_reverse_number_triangle(5)