def generate_right_aligned_alphabet_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    triangle_lines = []
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        letters = alphabet[:i]
        line = spaces + letters
        triangle_lines.append(line)
    return "\n".join(triangle_lines)

if __name__ == '__main__':
    sample_rows = 5
    result = generate_right_aligned_alphabet_triangle(sample_rows)
    print(result)