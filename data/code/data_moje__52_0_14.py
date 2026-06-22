def generate_diamond(size):
    lines = []
    for i in range(size):
        spaces = ' ' * (size - 1 - i)
        stars = '* ' * (i + 1)
        lines.append(spaces + stars.strip())
    for i in range(size - 2, -1, -1):
        spaces = ' ' * (size - 1 - i)
        stars = '* ' * (i + 1)
        lines.append(spaces + stars.strip())
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_diamond(5))