def print_alphabet_triangle(height):
    rows = []
    for i in range(1, height + 1):
        row_chars = []
        for j in range(i):
            char_code = ord('A') + j
            row_chars.append(chr(char_code))
        rows.append(" ".join(row_chars))
    return "\n".join(rows)

if __name__ == '__main__':
    height = 5
    result = print_alphabet_triangle(height)
    print(result)