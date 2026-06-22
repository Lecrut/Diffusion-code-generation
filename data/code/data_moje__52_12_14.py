def diamond(r):
    lines = []
    for i in range(-r, r + 1):
        width = r - abs(i)
        spaces = ' ' * width
        stars = '*' * (r * 2 - 2 * width + 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(diamond(3))