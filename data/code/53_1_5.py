def print_right_aligned_reverse_number_triangle(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        numbers = " ".join(str(j) for j in range(i, 0, -1))
        print(spaces + numbers)

if __name__ == '__main__':
    print_right_aligned_reverse_number_triangle(4)