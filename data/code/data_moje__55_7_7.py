def reverse_alphabet_triangle(start_char='Z', end_char='A'):
    rows = []
    current = start_char
    for i in range(ord(start_char) - ord(end_char), -1, -1):
        row = []
        for j in range(i + 1):
            row.append(current)
            current = chr((ord(current) - ord('A') + 1) % 26 + ord('A'))
        rows.append(' '.join(row))
    return '\n'.join(rows)

if __name__ == '__main__':
    print(reverse_alphabet_triangle('Z', 'A'))