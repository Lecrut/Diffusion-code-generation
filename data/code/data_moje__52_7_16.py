def generate_diamond_pattern(size):
    pattern_lines = []
    for i in range(1, size + 1):
        line = ' ' * (size - i) + '*' * (2 * i - 1)
        pattern_lines.append(line)
    for i in range(size - 1, 0, -1):
        line = ' ' * (size - i) + '*' * (2 * i - 1)
        pattern_lines.append(line)
    return '\n'.join(pattern_lines)

if __name__ == '__main__':
    print(generate_diamond_pattern(5))