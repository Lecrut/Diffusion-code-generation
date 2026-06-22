def generate_right_aligned_alphabet_triangle(num_rows):
    if num_rows <= 0:
        return ''
    lines = []
    for i in range(1, num_rows + 1):
        current_line = ''
        for j in range(1, i + 1):
            current_line += chr(ord('A') + j - 1)
        padding = ' ' * (num_rows - i)
        lines.append(padding + current_line)
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_values = [5, 7, 3]
    for num_rows in sample_values:
        result = generate_right_aligned_alphabet_triangle(num_rows)
        print(result)
        print('---')