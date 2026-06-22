def generate_right_aligned_pyramid(rows):
    lines = []
    for i in range(1, rows + 1):
        numbers = list(range(1, i + 1))
        line_text = ' '.join(map(str, numbers))
        line = line_text.rjust((rows * 2 - 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_right_aligned_pyramid(5)
    print(result)