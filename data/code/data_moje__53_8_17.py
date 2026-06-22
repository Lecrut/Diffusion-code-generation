def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row = []
        current_number = 1
        for j in range(1, i + 1):
            row.append(current_number)
            current_number += 1
        result.append(row)
    return result

if __name__ == '__main__':
    num_rows = 5
    triangle = generate_reverse_number_triangle(num_rows)
    print(triangle)