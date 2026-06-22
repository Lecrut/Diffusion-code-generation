def generate_alphabet_triangle(rows):
    if rows <= 0:
        return ""
    result_lines = []
    current_row = []
    char_code = ord('A')
    for i in range(1, rows + 1):
        for _ in range(i):
            current_row.append(chr(char_code))
            char_code += 1
            if char_code > ord('Z'):
                char_code = ord('A')
        result_lines.append("".join(current_row))
    return "\n".join(result_lines)

if __name__ == '__main__':
    sample_rows = 5
    print(generate_alphabet_triangle(sample_rows))