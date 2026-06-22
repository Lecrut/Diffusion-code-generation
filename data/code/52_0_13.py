def generate_diamond(size):
    lines = []
    for i in range(size):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(size - 2, -1, -1):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 5
    print(generate_diamond(sample_size))