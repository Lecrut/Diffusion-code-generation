def generate_alphabet_triangle():
    rows = 5
    lines = []
    for i in range(1, rows + 1):
        line_chars = []
        current_val = 65
        for j in range(i):
            line_chars.append(chr(current_val))
            current_val += 1
        lines.append("".join(line_chars))
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_alphabet_triangle())