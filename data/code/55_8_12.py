def generate_zigzag_alphabet_triangle(rows):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for i in range(rows):
        line_chars = []
        for col in range(i + 1):
            char_index = col % 26
            if i % 2 == 0:
                line_chars.append(alphabet[char_index])
            else:
                line_chars.append(alphabet[char_index])
        result.append(''.join(line_chars))
    return result

if __name__ == '__main__':
    sample_rows = 5
    pattern = generate_zigzag_alphabet_triangle(sample_rows)
    for line in pattern:
        print(line)