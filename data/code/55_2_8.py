def generate_alphabet_triangle():
    lines = []
    for i in range(1, 28):
        row = ''
        for j in range(i):
            char_code = 65 + (j + i - 2) % 26
            row += chr(char_code)
        lines.append(row)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_alphabet_triangle()
    print(result)