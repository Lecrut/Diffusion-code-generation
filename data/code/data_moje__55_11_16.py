def generate_alphabet_triangle(rows):
    result = []
    char_counter = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1, rows + 1):
        row_chars = []
        for j in range(i):
            char_index = char_counter % 26
            row_chars.append(alphabet[char_index])
            char_counter += 1
        result.append(" ".join(row_chars))
    return "\n".join(result)

if __name__ == '__main__':
    sample_rows = 5
    pattern = generate_alphabet_triangle(sample_rows)
    print(pattern)