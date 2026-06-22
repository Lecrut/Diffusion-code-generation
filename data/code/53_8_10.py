def generate_reverse_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row = list(range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    sample_rows = 5
    output = generate_reverse_triangle(sample_rows)
    print(output)