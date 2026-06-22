def generate_reverse_number_triangle(rows: int) -> list:
    if rows <= 0:
        return []
    result = []
    current_number = (rows * (rows + 1)) // 2
    for i in range(rows, 0, -1):
        line_numbers = []
        for _ in range(i):
            line_numbers.append(current_number)
            current_number -= 1
        result.append(line_numbers)
    return result

if __name__ == '__main__':
    sample_rows = 5
    triangle = generate_reverse_number_triangle(sample_rows)
    for line in triangle:
        print(" ".join(map(str, line)))