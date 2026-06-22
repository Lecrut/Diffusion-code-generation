def generate_right_aligned_reverse_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row_nums = [str(j) for j in range(1, i + 1)]
        line = ' '.join(row_nums)
        num_chars = len(line.replace(' ', ''))
        padding = rows - num_chars
        spaces = ' ' * (2 * padding + (rows - 1) * 2)
        formatted_line = spaces + line
        result.append(formatted_line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_right_aligned_reverse_triangle(4))