def generate_reverse_number_triangle(row_count):
    result_lines = []
    for i in range(row_count, 0, -1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        result_lines.append(line)
    return '\n'.join(result_lines)

if __name__ == '__main__':
    hardcoded_rows = 5
    triangle = generate_reverse_number_triangle(hardcoded_rows)
    print(triangle)