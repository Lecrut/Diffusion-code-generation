def generate_hollow_triangle(size: int) -> str:
    if size < 3:
        return ''
    lines = []
    lines.append('*' + ' ' * (size - 2) + '*')
    for i in range(1, size - 1):
        spaces = ' ' * (size - 1 - i)
        stars = '*' + ' ' * (2 * i - 1) + '*'
        line = spaces + stars
        lines.append(line)
    bottom = ' ' * (size - 1) + '*'
    lines.append(bottom)
    return '\n'.join(lines)
if __name__ == '__main__':
    print(generate_hollow_triangle(5))