def generate_alphabet_triangle(rows: int) -> list[str]:
    result = []
    current_char_code = ord('A')
    for i in range(1, rows + 1):
        row_chars = []
        for _ in range(i):
            row_chars.append(chr(current_char_code))
            current_char_code += 1
        result.append("".join(row_chars))
    return result

if __name__ == "__main__":
    sample_rows = 5
    print(generate_alphabet_triangle(sample_rows))