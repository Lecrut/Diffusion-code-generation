def generate_right_aligned_alphabet_triangle(rows):
    result_lines = []
    for i in range(1, rows + 1):
        chars = ""
        for j in range(1, i + 1):
            chars += chr(ord('A') + j - 1)
        line = " " * (rows - i) + chars
        result_lines.append(line)
    return "\n".join(result_lines)

if __name__ == '__main__':
    sample_rows = 5
    triangle = generate_right_aligned_alphabet_triangle(sample_rows)
    print(triangle)