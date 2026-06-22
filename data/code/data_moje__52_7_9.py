def generate_diamond_pattern(n):
    pattern_lines = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        pattern_lines.append(spaces + stars)
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        pattern_lines.append(spaces + stars)
    return '\n'.join(pattern_lines)

if __name__ == '__main__':
    n = 5
    print(generate_diamond_pattern(n))