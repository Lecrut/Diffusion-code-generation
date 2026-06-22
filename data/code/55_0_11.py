def generate_right_aligned_alphabet_triangle(height):
    result = []
    for i in range(1, height + 1):
        line_chars = []
        spaces = ' ' * (height - i)
        line_chars.append(spaces)
        alphabet_part = ''
        for j in range(i):
            char_code = ord('A') + j
            alphabet_part += chr(char_code)
        line_chars.append(alphabet_part)
        result.append(''.join(line_chars))
    return '\n'.join(result)

if __name__ == '__main__':
    sample_height = 5
    output = generate_right_aligned_alphabet_triangle(sample_height)
    print(output)