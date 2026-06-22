def generate_zigzag_triangle(rows):
    if rows < 1:
        return []
    result = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    current_char_index = 0
    for i in range(rows):
        row_chars = []
        for j in range(i + 1):
            char = alphabet[current_char_index % len(alphabet)]
            row_chars.append(char)
            current_char_index += 1
        if i % 2 == 1:
            row_chars.reverse()
        result.append(" ".join(row_chars))
    return result

if __name__ == '__main__':
    sample_rows = 7
    pattern = generate_zigzag_triangle(sample_rows)
    for line in pattern:
        print(line)