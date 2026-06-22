def generate_alphabet_triangle(height):
    result = []
    char_code = 65
    current_line = []
    for row in range(1, height + 1):
        line_chars = []
        for _ in range(row):
            line_chars.append(chr(char_code))
            char_code += 1
            if char_code > 90:
                char_code = 65
        result.append("".join(line_chars))
    return "\n".join(result)

if __name__ == '__main__':
    height = 5
    print(generate_alphabet_triangle(height))