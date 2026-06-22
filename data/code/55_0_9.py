def generate_right_aligned_alphabet_triangle(height):
    if height <= 0:
        return ''
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        chars = ''.join((chr(ord('A') + j) for j in range(i)))
        lines.append(spaces + chars)
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_height = 5
    result = generate_right_aligned_alphabet_triangle(sample_height)
    print(result)