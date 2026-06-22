def print_symmetric_reverse_number_triangle(rows):
    for i in range(rows, 0, -1):
        spaces = ' ' * (rows - i)
        left_half = ''.join(str(j) for j in range(1, i + 1))
        right_half = ''.join(str(j) for j in range(i - 1, 0, -1))
        print(spaces + left_half + right_half)

if __name__ == '__main__':
    print_symmetric_reverse_number_triangle(5)