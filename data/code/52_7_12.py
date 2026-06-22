def generate_diamond(n):
    lines = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return lines

def display_diamond(diamond_lines):
    for line in diamond_lines:
        print(line)

if __name__ == '__main__':
    diamond = generate_diamond(5)
    display_diamond(diamond)