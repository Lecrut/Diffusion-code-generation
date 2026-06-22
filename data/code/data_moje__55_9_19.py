def generate_mirrored_alphabet_triangle(rows: int) -> str:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lines = []
    for i in range(1, rows + 1):
        upper_part = alphabet[:i]
        lower_part = alphabet[i - 2::-1]
        line = upper_part + lower_part
        padding = ' ' * (rows - i)
        lines.append(padding + line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_mirrored_alphabet_triangle(5)
    print(result)