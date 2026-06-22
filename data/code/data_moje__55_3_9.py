def generate_inverted_alphabet_triangle(size=5):
    if size <= 0:
        return []
    result = []
    for i in range(size):
        row_chars = []
        for j in range(size):
            if j < i:
                row_chars.append(' ')
            else:
                row_chars.append(chr(ord('A') + size - 1 - i))
        result.append(''.join(row_chars))
    return result

if __name__ == '__main__':
    n = 5
    lines = generate_inverted_alphabet_triangle(n)
    for line in lines:
        print(line)