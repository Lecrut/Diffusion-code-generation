def reverse_number_triangle(rows: int) -> list[list[int]]:
    result = []
    for i in range(rows, 0, -1):
        row = [j for j in range(1, i + 1)]
        result.append(row)
    return result

if __name__ == '__main__':
    sample_rows = 5
    triangle = reverse_number_triangle(sample_rows)
    for row in triangle:
        print(" ".join(map(str, row)))