def generate_diamond(radius):
    lines = []
    for i in range(radius + 1):
        spaces = ' ' * (radius - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(radius - 1, -1, -1):
        spaces = ' ' * (radius - i)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond(3))