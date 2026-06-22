def reverse_triangle(start_char, end_char):
    chars = list(range(ord(start_char), ord(end_char) + 1))
    reversed_chars = chars[::-1]
    lines = []
    for i in range(1, len(reversed_chars) + 1):
        line = ''.join(chr(c) for c in reversed_chars[:i])
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = reverse_triangle('a', 'z')
    print(result)