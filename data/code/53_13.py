def generate_reverse_number_triangle(row_count):
    triangle = []
    for i in range(1, row_count + 1):
        row = []
        start = i * (i - 1) // 2 + 1
        for j in range(i):
            row.append(start + j)
        triangle.append(row)
    return triangle

if __name__ == '__main__':
    row_count = 5
    result = generate_reverse_number_triangle(row_count)
    for row in result:
        print(row)