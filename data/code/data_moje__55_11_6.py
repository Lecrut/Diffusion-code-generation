def generate_alphabet_triangle(rows):
    triangle = []
    current_char = ord('A')
    for i in range(1, rows + 1):
        row_chars = []
        for _ in range(i):
            row_chars.append(chr(current_char))
            current_char += 1
            if current_char > ord('Z'):
                current_char = ord('A')
        triangle.append(''.join(row_chars))
    return '\n'.join(triangle)

if __name__ == '__main__':
    rows = 5
    result = generate_alphabet_triangle(rows)
    print(result)