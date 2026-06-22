def print_triangle_pattern(rows):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result_lines = []
    for i in range(1, rows + 1):
        line = ''
        for j in range(1, i + 1):
            line += alphabet[(j - 1) % 26]
        result_lines.append(line)
    return '\n'.join(result_lines)

if __name__ == '__main__':
    sample_rows = 7
    pattern = print_triangle_pattern(sample_rows)
    print(pattern)