def print_alphabet_triangle(height):
    rows = []
    for i in range(1, height + 1):
        row_chars = []
        for j in range(i):
            char_code = 65 + j
            row_chars.append(chr(char_code))
        rows.append(' '.join(row_chars))
    result = '\n'.join(rows)
    print(result)
    return result

if __name__ == '__main__':
    HEIGHT = 5
    print_alphabet_triangle(HEIGHT)