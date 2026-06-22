def generate_reverse_number_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        row_nums = [str(rows - j) for j in range(i)]
        result.append(' '.join(row_nums))
    return result

if __name__ == '__main__':
    sample_rows = 5
    output = generate_reverse_number_triangle(sample_rows)
    print(output)