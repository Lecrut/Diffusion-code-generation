def generate_right_aligned_pyramid(rows):
    lines = []
    for i in range(1, rows + 1):
        row_vals = [str(j) for j in range(1, i + 1)]
        row_str = ' '.join(row_vals)
        line = row_str.rjust(rows * 2 - 1)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    rows = 5
    result = generate_right_aligned_pyramid(rows)
    print(result)