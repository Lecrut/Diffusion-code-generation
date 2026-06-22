def print_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = ' '.join(str(j) for j in range(i, 0, -1))
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    output_lines = print_reverse_number_triangle(sample_rows)
    for line in output_lines:
        print(line)