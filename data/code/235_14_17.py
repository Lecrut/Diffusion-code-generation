def zigzag_line(width, height):
    line = []
    for y in range(height):
        row = [' ' * x + '*' + ' ' * (width - 2 - x) if y % 2 == 0 else ' ' * (width - 1 - x) + '*' + ' ' * x for x in range(width)]
        line.append(''.join(row))
    return '\n'.join(line)

if __name__ == '__main__':
    print(zigzag_line(10, 5))