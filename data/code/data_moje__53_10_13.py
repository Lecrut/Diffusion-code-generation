def generate_reverse_number_triangle(rows: int) -> list:
    if rows < 1:
        return []
    result = []
    for i in range(rows, 0, -1):
        row = list(range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    sample_rows = 5
    pattern = generate_reverse_number_triangle(sample_rows)
    for line in pattern:
        print(*(line))