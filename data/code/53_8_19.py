def generate_reverse_number_triangle(num_rows):
    result = []
    for i in range(1, num_rows + 1):
        row = []
        for j in range(i):
            row.append(num_rows - j)
        result.append(row)
    return result

if __name__ == '__main__':
    rows = 5
    triangle = generate_reverse_number_triangle(rows)
    print(triangle)