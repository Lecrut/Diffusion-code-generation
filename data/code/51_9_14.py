def build_symmetric_pyramid(rows=6):
    pyramid = []
    for i in range(1, rows + 1):
        spaces = rows - i
        line = ' ' * spaces + str(i) * (2 * i - 1) + ' ' * spaces
        pyramid.append(line)
    return '\n'.join(pyramid)

if __name__ == '__main__':
    result = build_symmetric_pyramid(6)
    print(result)