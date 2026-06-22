def generate_reverse_number_triangle(rows=5):
    triangle = []
    for i in range(rows, 0, -1):
        row = []
        for j in range(i, 0, -1):
            row.append(j)
        triangle.append(row)
    return triangle

if __name__ == '__main__':
    result = generate_reverse_number_triangle()
    print(result)