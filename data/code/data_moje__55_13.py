def generate_alphabet_triangle(rows=5):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    triangle_lines = []
    for i in range(1, rows + 1):
        line = alphabet[0:i]
        triangle_lines.append(line)
    return "\n".join(triangle_lines)

if __name__ == '__main__':
    result = generate_alphabet_triangle(5)
    print(result)