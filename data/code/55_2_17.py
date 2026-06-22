def generate_alphabet_triangle(rows=None):
    if rows is None:
        rows = 6
    lines = []
    for i in range(1, rows + 1):
        line = []
        for j in range(1, i + 1):
            char_code = 64 + j
            line.append(chr(char_code))
        lines.append(''.join(line))
    return lines

if __name__ == '__main__':
    result = generate_alphabet_triangle()
    for line in result:
        print(line)