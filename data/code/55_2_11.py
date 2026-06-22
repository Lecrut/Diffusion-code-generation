def generate_alphabet_triangle():
    result = []
    for row in range(1, 10):
        line_chars = []
        for col in range(row):
            char_code = ord('A') + col
            line_chars.append(chr(char_code))
        result.append(' '.join(line_chars))
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_alphabet_triangle())