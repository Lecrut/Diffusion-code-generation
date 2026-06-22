def print_diamond(height):
    if height <= 0:
        return ''
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    for i in range(height - 1, 0, -1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = print_diamond(5)
    print(result)