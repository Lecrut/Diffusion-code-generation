def generate_reverse_number_triangle(rows):
    return [
        " ".join(str(num) for num in range(row, 0, -1))
        for row in range(rows, 0, -1)
    ]

if __name__ == '__main__':
    sample_rows = 5
    result = generate_reverse_number_triangle(sample_rows)
    for line in result:
        print(line)