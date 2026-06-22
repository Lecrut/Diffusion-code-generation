def print_triangle_letters(n):
    rows = []
    current_char_code = 65
    for i in range(1, n + 1):
        row_chars = []
        for _ in range(i):
            char = chr(current_char_code % 26 + 65)
            row_chars.append(char)
            current_char_code += 1
        rows.append(' '.join(row_chars))
    return '\n'.join(rows)

if __name__ == '__main__':
    print(print_triangle_letters(5))