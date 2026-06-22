def generate_mirrored_alphabet_triangle(rows):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result_lines = []
    for i in range(1, rows + 1):
        chars = alphabet[:i]
        mirrored = chars + chars[-2::-1]
        result_lines.append(mirrored)
    return '\n'.join(result_lines)

if __name__ == '__main__':
    sample_rows = 5
    pattern = generate_mirrored_alphabet_triangle(sample_rows)
    print(pattern)