def generate_inverted_alphabet_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line = ""
        current_char_code = ord('A')
        for _ in range(i):
            line += chr(current_char_code)
            current_char_code += 1
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    pattern = generate_inverted_alphabet_triangle(sample_rows)
    for line in pattern:
        print(line)