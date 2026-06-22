def reverse_alphabet_triangle(start_char='E', end_char='A'):
    chars = [chr(c) for c in range(ord(start_char), ord(end_char) - 1, -1)]
    lines = []
    for i, ch in enumerate(chars):
        lines.append(ch * (i + 1))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(reverse_alphabet_triangle())