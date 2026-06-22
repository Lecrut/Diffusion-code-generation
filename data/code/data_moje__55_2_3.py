def generate_alphabet_triangle(rows):
    result = []
    current_char_code = ord('A')
    for i in range(rows):
        line = []
        for j in range(i + 1):
            line.append(chr(current_char_code))
            current_char_code += 1
        result.append("".join(line))
    return "\n".join(result)

if __name__ == '__main__':
    sample_rows = 5
    print(generate_alphabet_triangle(sample_rows))