def create_symmetric_number_pyramid(levels):
    lines = []
    for i in range(1, levels + 1):
        line = ' '.join(str(min(i, levels - j + 1)) for j in range(1, 2 * i))
        lines.append(line.center(levels * 2 - 1))
    return '\n'.join(lines)

if __name__ == '__main__':
    result = create_symmetric_number_pyramid(4)
    print(result)