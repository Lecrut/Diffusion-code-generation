def print_diamond_pattern(height):
    if height % 2 == 0:
        height += 1
    half = height // 2
    lines = []
    for i in range(-half, half + 1):
        spaces = ' ' * (half - abs(i))
        stars = '*' * (2 * abs(i) + 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_diamond_pattern(7)
    print(result)