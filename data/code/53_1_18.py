def generate_right_aligned_reverse_number_triangle(rows):
    lines = []
    for i in range(rows, 0, -1):
        row_nums = [str(i) for i in range(1, i + 1)]
        row_str = ' '.join(row_nums)
        lines.append(row_str)
    max_len = max(len(line) for line in lines)
    right_aligned_lines = []
    for line in lines:
        right_aligned_lines.append(line.rjust(max_len))
    return '\n'.join(right_aligned_lines)

if __name__ == '__main__':
    num_rows = 4
    result = generate_right_aligned_reverse_number_triangle(num_rows)
    print(result)