def generate_diamond_pattern(n):
    lines = []
    for i in range(1, n + 1):
        stars = 2 * i - 1
        spaces = n - i
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    for i in range(n - 1, 0, -1):
        stars = 2 * i - 1
        spaces = n - i
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    return '\n'.join(lines)

def print_diamond(n):
    pattern = generate_diamond_pattern(n)
    print(pattern)
if __name__ == '__main__':
    print_diamond(5)