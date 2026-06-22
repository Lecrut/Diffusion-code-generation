def generate_right_aligned_alphabet_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lines = []
    for i in range(1, rows + 1):
        row_alphabet = alphabet[:i]
        padded_row = row_alphabet.rjust(rows)
        lines.append(padded_row)
    return lines

if __name__ == '__main__':
    sample_rows = 5
    result = generate_right_aligned_alphabet_triangle(sample_rows)
    for line in result:
        print(line)