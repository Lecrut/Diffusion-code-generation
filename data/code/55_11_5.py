def generate_alphabet_triangle(n):
    result = []
    current_char = 'A'
    for i in range(1, n + 1):
        row = ''
        for _ in range(i):
            row += current_char
            current_char = chr(ord(current_char) + 1)
            if current_char > 'Z':
                current_char = 'A'
        result.append(row)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_alphabet_triangle(5))