def generate_symmetric_reverse_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        left = list(range(i, 0, -1))
        right = list(range(2, i + 1))
        full_row = left + right
        row_str = ' '.join(map(str, full_row))
        result.append(row_str)
    return result

if __name__ == '__main__':
    triangle = generate_symmetric_reverse_triangle(5)
    for line in triangle:
        print(line)