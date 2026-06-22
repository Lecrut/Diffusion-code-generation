def generate_diamond(n):
    half = n
    lines = []
    for i in range(1, half + 1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(half - 1, 0, -1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond(6))