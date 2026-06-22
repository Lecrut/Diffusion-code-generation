def generate_alphabet_triangle(rows):
    if rows <= 0:
        return []
    triangle = []
    char_counter = 0
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(1, rows + 1):
        row_chars = []
        for j in range(i):
            row_chars.append(chars[char_counter % 26])
            char_counter += 1
        triangle.append(''.join(row_chars))
    return triangle
if __name__ == '__main__':
    sample_rows = 5
    result = generate_alphabet_triangle(sample_rows)
    print(result)