def generate_triangle_pattern(n):
    if n <= 0:
        return ''
    result_lines = []
    for i in range(1, n + 1):
        line = ''
        for j in range(i):
            letter_index = (i + j) % 26
            if letter_index == 0:
                letter = 'Z'
            else:
                letter = chr(ord('A') + letter_index - 1)
            line += letter + ' '
        result_lines.append(line.rstrip())
    return '\n'.join(result_lines)
if __name__ == '__main__':
    sample_size = 5
    pattern = generate_triangle_pattern(sample_size)
    print(pattern)