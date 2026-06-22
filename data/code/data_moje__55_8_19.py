def generate_zigzag_alphabet_triangle(rows):
    if rows <= 0:
        return []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    current_char_index = 0
    for i in range(rows):
        row_chars = []
        for _ in range(i + 1):
            row_chars.append(alphabet[current_char_index % 26])
            current_char_index += 1
        if i % 2 == 1:
            row_chars.reverse()
        result.append("".join(row_chars))
    return result

if __name__ == '__main__':
    sample_rows = 6
    pattern = generate_zigzag_alphabet_triangle(sample_rows)
    for line in pattern:
        print(line)