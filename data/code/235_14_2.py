def zigzag_line(width, height):
    pattern = []
    for y in range(height):
        line = [' ' * x + '*' + ' ' * (width - x - 1) for x in range(y + 1)]
        if y % 2 == 1:
            line.reverse()
        pattern.extend(line)
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(zigzag_line(5, 3))