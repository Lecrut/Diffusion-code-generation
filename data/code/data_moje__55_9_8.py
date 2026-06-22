def generate_mirrored_alphabet_triangle(rows=5):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for i in range(1, rows + 1):
        left = alphabet[:i]
        right = alphabet[i - 2::-1]
        line = left + right
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = generate_mirrored_alphabet_triangle()
    for line in result:
        print(line)