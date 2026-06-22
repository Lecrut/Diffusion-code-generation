def create_symmetric_pyramid(levels=4):
    lines = []
    for i in range(1, levels + 1):
        line = ' ' * (levels - i) + str(i) * (2 * i - 1)
        lines.append(line)
    for i in range(levels - 1, 0, -1):
        line = ' ' * (levels - i) + str(i) * (2 * i - 1)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(create_symmetric_pyramid(4))