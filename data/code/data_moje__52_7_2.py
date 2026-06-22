def generate_diamond_pattern(size):
    lines = []
    max_width = 2 * size - 1
    for i in range(1, size + 1):
        stars = '*' * (2 * i - 1)
        spaces = (max_width - len(stars)) // 2
        lines.append(' ' * spaces + stars)
    for i in range(size - 1, 0, -1):
        stars = '*' * (2 * i - 1)
        spaces = (max_width - len(stars)) // 2
        lines.append(' ' * spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_diamond_pattern(5)
    print(result)