def print_right_aligned_triangle(row_count):
    result = []
    for i in range(1, row_count + 1):
        line = ' ' * (row_count - i) + '*' * i
        result.append(line)
    for line in result:
        print(line)

if __name__ == '__main__':
    count = 10
    print_right_aligned_triangle(count)