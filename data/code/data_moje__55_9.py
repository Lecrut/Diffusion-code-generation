def generate_mirrored_alphabet_triangle(rows):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pattern_lines = []
    for i in range(1, rows + 1):
        left_part = alphabet[:i]
        right_part = alphabet[1:i][::-1]
        line = left_part + right_part
        pattern_lines.append(line)
    return '\n'.join(pattern_lines)

if __name__ == '__main__':
    result = generate_mirrored_alphabet_triangle(5)
    print(result)