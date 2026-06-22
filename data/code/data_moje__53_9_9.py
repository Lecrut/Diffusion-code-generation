def print_reverse_number_triangle(height=5):
    for i in range(height, 0, -1):
        print(''.join((str(j) for j in range(1, i + 1))))
if __name__ == '__main__':
    print_reverse_number_triangle(5)