def hollow_alphabet_triangle(base_width):
    result_lines = []
    for i in range(1, base_width + 1):
        row_chars = []
        for j in range(1, base_width + 1):
            if j <= i:
                if i == 1 or i == base_width or j == 1 or j == i:
                    char_code = ord('A') + (i - 1)
                    row_chars.append(chr(char_code))
                else:
                    row_chars.append(' ')
            else:
                row_chars.append(' ')
        result_lines.append(''.join(row_chars))
    return '\n'.join(result_lines)

if __name__ == '__main__':
    sample_width = 5
    result = hollow_alphabet_triangle(sample_width)
    print(result)