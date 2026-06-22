def generate_reverse_number_triangle(rows):
    triangle = []
    for i in range(rows, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(j)
        triangle.append(row)
    return triangle

if __name__ == '__main__':
    result = generate_reverse_number_triangle(5)
    for row in result:
        print(' '.join(map(str, row)))