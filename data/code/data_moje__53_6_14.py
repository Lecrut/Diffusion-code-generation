def generate_reverse_number_triangle(height: int) -> str:
    rows = []
    for i in range(height, 0, -1):
        row_numbers = []
        for j in range(1, i + 1):
            row_numbers.append(str(j))
        rows.append(' '.join(row_numbers))
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_reverse_number_triangle(4))