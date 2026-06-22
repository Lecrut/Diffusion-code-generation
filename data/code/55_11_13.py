def generate_alphabet_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        start_char = ord('A') + sum(range(i - 1))
        row_chars = []
        for j in range(i):
            row_chars.append(chr(start_char + j))
        result.append("".join(row_chars))
    return result

if __name__ == '__main__':
    sample_rows = 5
    printed_lines = generate_alphabet_triangle(sample_rows)
    for line in printed_lines:
        print(line)