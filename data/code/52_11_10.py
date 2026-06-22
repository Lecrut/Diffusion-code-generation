def generate_diamond_pattern(size):
    if size % 2 == 0:
        size += 1
    lines = []
    half = size // 2
    for i in range(-half, half + 1):
        stars_count = size - 2 * abs(i)
        spaces_count = abs(i)
        line = ' ' * spaces_count + '*' * stars_count
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = generate_diamond_pattern(7)
    print(result)