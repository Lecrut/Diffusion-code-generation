def generate_zigzag_triangle(rows: int) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for i in range(rows):
        row_chars = []
        for j in range(i + 1):
            if i % 2 == 0:
                char_index = i * (i + 1) // 2 + j
            else:
                char_index = i * (i + 1) // 2 + (i - j)
            char_index = char_index % 26
            row_chars.append(alphabet[char_index])
        result.append(' '.join(row_chars))
    return '\n'.join(result)
if __name__ == '__main__':
    num_rows = 5
    print(generate_zigzag_triangle(num_rows))