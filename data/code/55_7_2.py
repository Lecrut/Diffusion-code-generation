def reverse_alphabet_triangle():
    start_char = 'a'
    end_char = 'z'
    start_ord = ord(start_char)
    end_ord = ord(end_char)
    chars = [chr(c) for c in range(end_ord, start_ord - 1, -1)]
    lines = []
    for i in range(len(chars)):
        line = ''.join(chars[j] for j in range(i, -1, -1))
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = reverse_alphabet_triangle()
    print('\n'.join(result))