def reverse_alphabet_triangle(start_char='A', end_char='Z'):
    alphabet = [chr(i) for i in range(ord(start_char), ord(end_char) + 1)]
    reversed_alphabet = alphabet[::-1]
    lines = []
    for i in range(1, len(reversed_alphabet) + 1):
        line = ''.join(reversed_alphabet[:i])
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = reverse_alphabet_triangle('A', 'Z')
    print(result)