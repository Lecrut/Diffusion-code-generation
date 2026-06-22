def generate_alphabet_triangle(n: int) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lines = []
    for i in range(1, n + 1):
        line_chars = []
        for j in range(i):
            char_index = (i + j - 1) % 26
            line_chars.append(alphabet[char_index])
        lines.append(''.join(line_chars))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_alphabet_triangle(5))