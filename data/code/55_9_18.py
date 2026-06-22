def generate_mirrored_alphabet_triangle(rows):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pattern_lines = []
    for i in range(1, rows + 1):
        left_part = alphabet[:i][::-1]
        right_part = alphabet[1:i]
        line = left_part + right_part
        pattern_lines.append(line)
    return '\n'.join(pattern_lines)

if __name__ == '__main__':
    hardcoded_rows = 5
    result = generate_mirrored_alphabet_triangle(hardcoded_rows)
    print(result)