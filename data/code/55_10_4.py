def alphabet_triangle(height: int) -> str:
    if height <= 0:
        return ''
    lines = []
    for i in range(height):
        row_chars = []
        for j in range(i + 1):
            char_code = ord('A') + j
            row_chars.append(chr(char_code))
        line = ''.join(row_chars)
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_height = 5
    result = alphabet_triangle(sample_height)
    print(result)