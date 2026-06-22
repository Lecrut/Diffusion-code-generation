def generate_reverse_number_triangle(rows=5):
    result = []
    start_num = rows
    for row_idx in range(rows):
        row = []
        for col_idx in range(row_idx + 1):
            row.append(start_num)
            start_num -= 1
        result.append(row)
        start_num -= 1
    return result

if __name__ == '__main__':
    triangle = generate_reverse_number_triangle(5)
    print(triangle)