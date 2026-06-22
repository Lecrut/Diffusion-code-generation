def print_alphabet_triangle(size):
    lines = []
    for i in range(1, size + 1):
        line_chars = []
        current = ord('A')
        for j in range(i):
            line_chars.append(chr(current))
            current = (current - ord('A') + 1) % 26 + ord('A')
        lines.append("".join(line_chars))
    return "\n".join(lines)

if __name__ == '__main__':
    sample_size = 5
    result = print_alphabet_triangle(sample_size)
    print(result)