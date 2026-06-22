def generate_left_aligned_alphabet_triangle():
    lines = []
    for i in range(1, 27):
        row_chars = []
        for j in range(1, i + 1):
            ascii_val = 64 + j
            char = chr(ascii_val)
            row_chars.append(char)
        lines.append(' '.join(row_chars))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_left_aligned_alphabet_triangle())