def generate_diamond_pattern(size=5):
    pattern = []
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        pattern.append(spaces + stars)
    for i in range(size - 1, 0, -1):
        spaces = ' ' * (size - i)
        stars = '*' * (2 * i - 1)
        pattern.append(spaces + stars)
    return '\n'.join(pattern)
if __name__ == '__main__':
    size = 5
    diamond = generate_diamond_pattern(size)
    print(diamond)