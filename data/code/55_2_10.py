def generate_alphabet_triangle(rows=None):
    if rows is None:
        rows = 26
    result = []
    for i in range(1, rows + 1):
        line_chars = []
        for j in range(i):
            char_code = ord('A') + j
            line_chars.append(chr(char_code))
        result.append(''.join(line_chars))
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_alphabet_triangle(5))