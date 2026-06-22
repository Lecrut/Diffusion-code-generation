def generate_alphabet_triangle(rows):
    result = []
    char_code = ord('A')
    for i in range(1, rows + 1):
        row_chars = []
        for j in range(i):
            row_chars.append(chr(char_code))
            char_code += 1
        result.append(''.join(row_chars))
    return '\n'.join(result)

if __name__ == '__main__':
    sample_rows = 5
    triangle = generate_alphabet_triangle(sample_rows)
    print(triangle)