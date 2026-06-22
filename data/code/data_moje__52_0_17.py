def generate_diamond_pattern(size):
    lines = []
    for i in range(size):
        spaces = ' ' * (size - i - 1)
        stars = '* ' * (i + 1)
        lines.append(spaces + stars.rstrip())
    for i in range(size - 2, -1, -1):
        spaces = ' ' * (size - i - 1)
        stars = '* ' * (i + 1)
        lines.append(spaces + stars.rstrip())
    return '\n'.join(lines)

if __name__ == '__main__':
    size = 5
    pattern = generate_diamond_pattern(size)
    print(pattern)