def generate_alphabet_triangle(rows):
    result = []
    char_code = 65
    for i in range(1, rows + 1):
        row_chars = [chr((char_code + j) % 26 + 65) for j in range(i)]
        result.append(''.join(row_chars))
        char_code = (char_code + i) % 26 + 65
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_alphabet_triangle(5))