def generate_alphabet_triangle(height):
    result = []
    current_chars = []
    for i in range(height):
        current_chars.append(chr(65 + i % 26))
        row_str = ''.join(current_chars)
        result.append(row_str)
    return '\n'.join(result)

if __name__ == '__main__':
    height = 5
    output = generate_alphabet_triangle(height)
    print(output)