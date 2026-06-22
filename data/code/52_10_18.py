def generate_diamond(size):
    if size <= 0:
        return ''
    rows = 2 * size - 1
    lines = []
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
    print('Diamond of size 1:')
    print(generate_diamond(1))
    print('\nDiamond of size 3:')
    print(generate_diamond(3))
    print('\nDiamond of size 5:')
    print(generate_diamond(5))
    print('\nDiamond of size 0 (empty):')
    print(repr(generate_diamond(0)))
    print('\nDiamond of size -1 (invalid, empty):')
    print(repr(generate_diamond(-1)))