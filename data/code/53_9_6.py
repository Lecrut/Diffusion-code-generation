def print_reverse_number_triangle(height):
    for i in range(height, 0, -1):
        line = ''
        for j in range(i, 0, -1):
            line += str(j)
        print(line)

if __name__ == '__main__':
    print_reverse_number_triangle(5)