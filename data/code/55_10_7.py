def alphabet_triangle(height):
    if height <= 0:
        return ''
    height = min(height, 26)
    lines = []
    for i in range(1, height + 1):
        line = ' '.join((chr(64 + j) for j in range(1, i + 1)))
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_height = 5
    result = alphabet_triangle(sample_height)
    print(result)