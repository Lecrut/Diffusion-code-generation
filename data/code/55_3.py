def inverted_alphabet_triangle(rows=5):
    lines = []
    for i in range(rows, 0, -1):
        chars = [chr(ord('A') + j) for j in range(i)]
        line = ' '.join(chars)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(inverted_alphabet_triangle())