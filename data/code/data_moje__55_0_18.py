def generate_right_aligned_alphabet_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_lines = []
    for i in range(1, rows + 1):
        letters = alphabet[:i]
        line = letters.rjust(rows)
        result_lines.append(line)
    return "\n".join(result_lines)

if __name__ == '__main__':
    sample_rows = 5
    triangle = generate_right_aligned_alphabet_triangle(sample_rows)
    print(triangle)