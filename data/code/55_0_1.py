def generate_right_aligned_alphabet_triangle(rows):
    result_lines = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1, rows + 1):
        letters = alphabet[:i]
        line = letters.rjust(rows)
        result_lines.append(line)
    return result_lines

if __name__ == '__main__':
    sample_rows = 6
    pattern = generate_right_aligned_alphabet_triangle(sample_rows)
    for line in pattern:
        print(line)