def generate_zigzag_triangle(rows: int) -> list[str]:
    result = []
    alphabet = [chr(i) for i in range(65, 91)]
    for i in range(1, rows + 1):
        row_chars = []
        for j in range(1, i + 1):
            char_index = (j - 1) % 26
            if j % 2 == 0:
                char_index = (char_index + 1) % 26
            row_chars.append(alphabet[char_index])
        result.append(" ".join(row_chars))
    return result

if __name__ == '__main__':
    for line in generate_zigzag_triangle(5):
        print(line)