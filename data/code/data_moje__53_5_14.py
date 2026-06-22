def print_symmetric_reverse_triangle(rows):
    for i in range(rows, 0, -1):
        left_part = "".join(str(j) for j in range(i, 0, -1))
        right_part = "".join(str(j) for j in range(1, i))
        print(left_part + right_part)

if __name__ == '__main__':
    n = 5
    print_symmetric_reverse_triangle(n)