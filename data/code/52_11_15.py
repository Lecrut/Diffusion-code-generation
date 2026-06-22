def generate_diamond(n):
    if n <= 0:
        return ""
    lines = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 5
    result = generate_diamond(sample_size)
    print(result)