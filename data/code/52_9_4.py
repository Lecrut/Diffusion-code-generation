def generate_diamond_pattern(half_height):
    lines = []
    for i in range(1, half_height + 1):
        line = ' ' * (half_height - i) + '*' * (2 * i - 1)
        lines.append(line)
    for i in range(half_height - 1, 0, -1):
        line = ' ' * (half_height - i) + '*' * (2 * i - 1)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_diamond_pattern(4)
    print(result)