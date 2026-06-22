def print_centered_alphabet_triangle(height: int = 5) -> str:
    lines = []
    for i in range(height):
        chars = [chr(ord('A') + j) for j in range(i + 1)]
        line_chars = []
        for k, c in enumerate(chars):
            line_chars.append(c)
            if k < len(chars) - 1:
                line_chars.append(' ')
        line_str = ''.join(line_chars)
        padding = ' ' * (height - 1 - i)
        lines.append(padding + line_str)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_centered_alphabet_triangle(5)
    print(result)