def generate_diamond(width):
    lines = []
    for i in range(width):
        spaces = abs((width - 1) // 2 - i)
        stars = width - 2 * spaces
        line = [' ' for _ in range(spaces)] + ['*' for _ in range(stars)] + [' ' for _ in range(spaces)]
        lines.append(''.join(line))
    return lines

if __name__ == '__main__':
    width = 9
    result = generate_diamond(width)
    for line in result:
        print(line)