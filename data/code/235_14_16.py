def zigzag_line(width, height):
    line = []
    for y in range(height):
        for x in range(width):
            if (x + y) % 2 == 0:
                line.append('*')
            else:
                line.append(' ')
        line.append('\n')
    return ''.join(line)

if __name__ == '__main__':
    print(zigzag_line(10, 5))