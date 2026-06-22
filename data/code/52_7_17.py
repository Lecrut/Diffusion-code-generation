def generate_diamond_pattern(n):
    lines = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_diamond_pattern(5)
    print(result)