def generate_mirrored_alphabet_triangle(rows):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper = alphabet.upper()
    lines = []
    for i in range(1, rows + 1):
        part = upper[:i]
        left = part[::-1]
        right = part[1:]
        line = left + right
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_rows = 5
    result = generate_mirrored_alphabet_triangle(sample_rows)
    print(result)