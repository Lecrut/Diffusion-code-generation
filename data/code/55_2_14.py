def generate_alphabet_triangle():
    rows = 5
    result = []
    for i in range(1, rows + 1):
        line_chars = []
        for j in range(i):
            char_code = ord('A') + j
            char = chr(char_code)
            line_chars.append(char)
        result.append(''.join(line_chars))
    return result

if __name__ == '__main__':
    lines = generate_alphabet_triangle()
    for line in lines:
        print(line)