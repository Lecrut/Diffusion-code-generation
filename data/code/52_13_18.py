def generate_diamond_pattern(height):
    if height % 2 == 0:
        height += 1
    half = height // 2
    lines = []
    for i in range(height):
        if i <= half:
            spaces = ' ' * (half - i)
            stars = '*' * (2 * i + 1)
            lines.append(spaces + stars)
        else:
            spaces = ' ' * (i - half)
            stars = '*' * (2 * (height - 1 - i) + 1)
            lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_height = 7
    result = generate_diamond_pattern(sample_height)
    print(result)