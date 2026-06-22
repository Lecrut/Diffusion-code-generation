def print_alphabet_triangle(rows):
    if rows < 1:
        return
    current_char_code = ord('A')
    for i in range(1, rows + 1):
        line_chars = []
        for _ in range(i):
            if current_char_code > ord('Z'):
                current_char_code = ord('A')
            line_chars.append(chr(current_char_code))
            current_char_code += 1
        print(' '.join(line_chars))

if __name__ == '__main__':
    sample_rows = 7
    print_alphabet_triangle(sample_rows)