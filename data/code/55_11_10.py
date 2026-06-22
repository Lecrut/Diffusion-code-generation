def generate_alphabet_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_lines = []
    for i in range(1, rows + 1):
        current_row = []
        for j in range(i):
            char_index = j % 26
            current_row.append(alphabet[char_index])
        result_lines.append("".join(current_row))
    return "\n".join(result_lines)

if __name__ == '__main__':
    sample_rows = 5
    output = generate_alphabet_triangle(sample_rows)
    print(output)