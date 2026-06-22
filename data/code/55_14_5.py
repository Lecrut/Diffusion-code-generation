def generate_alphabet_triangle(rows=5):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(1, rows + 1):
        line_chars = alphabet[:i]
        reversed_chars = line_chars[-2::-1]
        middle_part = line_chars[0] + reversed_chars
        padding = " " * (rows - i)
        result.append(padding + middle_part + padding)
    return result

if __name__ == '__main__':
    triangle = generate_alphabet_triangle(5)
    for line in triangle:
        print(line)