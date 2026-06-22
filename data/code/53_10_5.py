def generate_reverse_number_triangle(rows: int) -> list:
    result = []
    for i in range(rows, 0, -1):
        row = list(range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    sample_rows = 5
    triangle = generate_reverse_number_triangle(sample_rows)
    for row in triangle:
        print(row)