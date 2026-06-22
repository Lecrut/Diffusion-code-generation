def generate_alphabet_triangle(rows):
    result = []
    current_char_code = 65
    for i in range(1, rows + 1):
        row_chars = []
        for _ in range(i):
            row_chars.append(chr(current_char_code))
            current_char_code = (current_char_code - 64) % 26 + 65
        result.append(" ".join(row_chars))
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_alphabet_triangle(5))