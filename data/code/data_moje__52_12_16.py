def diamond(r):
    lines = []
    for i in range(-r, r + 1):
        spaces = abs(i)
        stars = 2 * (r - abs(i)) + 1
        lines.append(' ' * spaces + '*' * stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(diamond(3))