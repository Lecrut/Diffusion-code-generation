def generate_alphabet_triangle():
    rows = 5
    lines = []
    for i in range(1, rows + 1):
        row_chars = []
        for j in range(i):
            char_code = ord('A') + j
            row_chars.append(chr(char_code))
        lines.append(''.join(row_chars))
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_alphabet_triangle()
    print(result)