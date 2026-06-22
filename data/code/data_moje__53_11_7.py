def get_reverse_number_triangle(height: int) -> list[str]:
    rows = []
    for i in range(height, 0, -1):
        row_numbers = []
        for j in range(1, i + 1):
            row_numbers.append(str(j))
        rows.append(" ".join(row_numbers))
    return rows

if __name__ == '__main__':
    HEIGHT = 5
    result = get_reverse_number_triangle(HEIGHT)
    for row in result:
        print(row)