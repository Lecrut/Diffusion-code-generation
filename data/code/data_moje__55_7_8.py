def reverse_alphabet_triangle(start_char, end_char):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    start_index = alphabet.index(start_char.lower())
    end_index = alphabet.index(end_char.lower())
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    selected = alphabet[start_index:end_index + 1]
    reversed_selected = selected[::-1]
    lines = []
    for i in range(1, len(reversed_selected) + 1):
        line = ''.join(reversed_selected[:i])
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = reverse_alphabet_triangle('a', 'e')
    print(result)