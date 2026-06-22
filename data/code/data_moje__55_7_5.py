def reverse_alphabet_triangle():
    start_char = 'A'
    end_char = 'Z'
    chars = list(chr(c) for c in range(ord(start_char), ord(end_char) + 1))
    reversed_chars = chars[::-1]
    lines = []
    for i in range(len(reversed_chars)):
        line = ''.join(reversed_chars[:i + 1])
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(reverse_alphabet_triangle())