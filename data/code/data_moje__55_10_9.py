def print_alphabet_triangle(height: int) -> str:
    lines = []
    for i in range(1, height + 1):
        line_chars = []
        for j in range(i):
            line_chars.append(chr(ord('A') + j))
        line = " ".join(line_chars)
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    HEIGHT = 5
    result = print_alphabet_triangle(HEIGHT)
    print(result)