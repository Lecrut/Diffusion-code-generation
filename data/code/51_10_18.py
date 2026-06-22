def generate_number_pyramid():
    height = 5
    result = []
    for i in range(1, height + 1):
        row_numbers = [str(j) for j in range(1, i + 1)]
        row_str = ' '.join(row_numbers)
        result.append(row_str)
    max_width = max(len(row) for row in result)
    py_lines = []
    for row in result:
        py_lines.append(f"{row:^{max_width}}")
    return '\n'.join(py_lines)

if __name__ == '__main__':
    print(generate_number_pyramid())