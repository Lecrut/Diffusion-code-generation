def generate_diamond(size):
    lines = []
    if size <= 0:
        return ""
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(size - 1, 0, -1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond(5))