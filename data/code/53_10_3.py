def generate_reverse_number_triangle(rows: int) -> list[str]:
    if rows <= 0:
        return []
    result = []
    for i in range(rows, 0, -1):
        row = ' '.join(str(j) for j in range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    sample_rows = 5
    output = generate_reverse_number_triangle(sample_rows)
    for line in output:
        print(line)