def generate_alphabet_triangle(rows):
    result = []
    current_char_code = ord('A')
    for i in range(rows):
        row_chars = []
        for j in range(i + 1):
            row_chars.append(chr(current_char_code))
            current_char_code += 1
        result.append("".join(row_chars))
    return result

if __name__ == '__main__':
    sample_rows = 5
    triangle = generate_alphabet_triangle(sample_rows)
    for line in triangle:
        print(line)