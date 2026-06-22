def generate_alphabet_triangle(size: int) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lines = []
    current_idx = 0
    for i in range(1, size + 1):
        row_chars = []
        for j in range(i):
            char = alphabet[current_idx % 26]
            row_chars.append(char)
            current_idx += 1
        lines.append(''.join(row_chars))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_alphabet_triangle(5))