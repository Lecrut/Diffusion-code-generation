def generate_alphabet_triangle(rows):
    result = []
    current_char_code = ord('A')
    for i in range(1, rows + 1):
        row_chars = [chr(current_char_code + j) for j in range(i)]
        result.append("".join(row_chars))
        current_char_code += i
    return "\n".join(result)

if __name__ == "__main__":
    sample_rows = 7
    print(generate_alphabet_triangle(sample_rows))