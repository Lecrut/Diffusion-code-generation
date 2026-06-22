def build_inverted_alphabet_triangle(rows):
    result = []
    current_char_code = ord('Z')
    for i in range(rows):
        line_chars = []
        for j in range(rows - i):
            line_chars.append(chr(current_char_code))
            current_char_code -= 1
        result.append("".join(line_chars))
    return result

if __name__ == '__main__':
    sample_rows = 5
    output = build_inverted_alphabet_triangle(sample_rows)
    for line in output:
        print(line)