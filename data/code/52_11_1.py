def build_diamond_pattern(size):
    lines = []
    for i in range(-size + 1, size):
        spaces = ' ' * abs(i)
        stars = '*' * (2 * (size - abs(i)) - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = build_diamond_pattern(5)
    print(result)