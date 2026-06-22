def diamond(r):
    lines = []
    for i in range(-r, r + 1):
        width = r - abs(i)
        stars = 2 * (r - width) + 1
        line = ' ' * width + '*' * stars
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    r = 3
    print(diamond(r))