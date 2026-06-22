def generate_inverted_alphabet_triangle(n):
    result = []
    for i in range(n):
        row = []
        for j in range(i):
            row.append(chr(ord('A') + (i - j - 1)))
        row.append(chr(ord('A') + n - i - 1))
        for j in range(i):
            row.append(chr(ord('A') + j))
        result.append(' '.join(row))
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_inverted_alphabet_triangle(5))