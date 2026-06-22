def generate_diamond(n: int) -> list[str]:
    lines = []
    for i in range(n):
        spaces = ' ' * (n - 1 - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - 1 - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    return lines

if __name__ == '__main__':
    size = 5
    diamond_pattern = generate_diamond(size)
    for line in diamond_pattern:
        print(line)