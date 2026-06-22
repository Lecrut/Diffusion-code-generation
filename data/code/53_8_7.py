def generate_reverse_number_triangle(num_rows):
    result = []
    for i in range(num_rows, 0, -1):
        row = list(range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    rows = 5
    triangle = generate_reverse_number_triangle(rows)
    print(triangle)