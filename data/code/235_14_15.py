def zigzag_line(width, height):
    for y in range(height):
        line = []
        for x in range(width):
            if (x + y) % 2 == 0:
                line.append('*')
            else:
                line.append(' ')
        print(''.join(line))

if __name__ == '__main__':
    zigzag_line(10, 5)