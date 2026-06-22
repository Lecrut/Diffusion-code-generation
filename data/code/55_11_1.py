def generate_alphabet_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if rows > len(alphabet):
        rows = len(alphabet)
    result = []
    current_char_index = 0
    for i in range(rows):
        row_chars = []
        for _ in range(i + 1):
            row_chars.append(alphabet[current_char_index])
            current_char_index += 1
        result.append("".join(row_chars))
    return "\n".join(result)

if __name__ == "__main__":
    sample_rows = 5
    print(generate_alphabet_triangle(sample_rows))