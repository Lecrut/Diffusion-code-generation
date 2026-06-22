def generate_diamond(n: int) -> str:
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
    n = 5
    result = generate_diamond(n)
    print(result)