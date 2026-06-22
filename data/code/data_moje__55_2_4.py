def generate_alphabet_triangle(rows):
    result = []
    current_char_code = ord('A')
    for row in range(1, rows + 1):
        line_chars = []
        for _ in range(row):
            line_chars.append(chr(current_char_code))
            current_char_code += 1
            if current_char_code > ord('Z'):
                current_char_code = ord('A')
        result.append("".join(line_chars))
    return result

if __name__ == '__main__':
    sample_rows = 7
    triangle = generate_alphabet_triangle(sample_rows)
    for line in triangle:
        print(line)