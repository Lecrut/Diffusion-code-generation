def create_reverse_number_triangle(n):
    rows = []
    for i in range(n, 0, -1):
        row_numbers = list(range(1, i + 1))
        row_str = ' '.join(map(str, row_numbers))
        rows.append(row_str)
    return '\n'.join(rows)

if __name__ == '__main__':
    sample_size = 5
    result = create_reverse_number_triangle(sample_size)
    print(result)