def reverse_alphabet_triangle(start_char, end_char):
    chars = list(range(ord(start_char.upper()), ord(end_char.upper()) + 1))
    lines = []
    for i in range(len(chars)):
        line_chars = [chr(c) for c in chars[:i+1]]
        line = ''.join(line_chars)
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = reverse_alphabet_triangle('A', 'E')
    for line in result:
        print(line)