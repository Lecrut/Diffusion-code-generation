def print_alphabet_triangle(height):
    if height <= 0:
        return ''
    lines = []
    for i in range(1, height + 1):
        row = ''
        for j in range(i):
            row += chr(ord('A') + j)
        lines.append(row)
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_height = 5
    result = print_alphabet_triangle(sample_height)
    print(result)