def generate_diamond(n):
    lines = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '* ' * (i + 1)
        lines.append(spaces + stars.strip())
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        stars = '* ' * (i + 1)
        lines.append(spaces + stars.strip())
    return '\n'.join(lines)

if __name__ == '__main__':
    n = 6
    print(generate_diamond(n))