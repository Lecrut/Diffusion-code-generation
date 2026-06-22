def generate_zigzag_triangle(rows):
    result = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for row in range(rows):
        line_chars = []
        for col in range(row + 1):
            char_index = (row * 3 + col) % 26
            line_chars.append(alphabet[char_index])
        result.append(" ".join(line_chars))
    return "\n".join(result)

if __name__ == "__main__":
    sample_rows = 5
    print(generate_zigzag_triangle(sample_rows))