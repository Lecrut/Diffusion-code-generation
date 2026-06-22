def create_symmetric_pyramid(levels):
    pyramid_lines = []
    for i in range(1, levels + 1):
        left_side = ''.join(str(j) for j in range(1, i + 1))
        right_side = ''.join(str(j) for j in range(i - 1, 0, -1))
        line = left_side + right_side
        pyramid_lines.append(line)
    return '\n'.join(pyramid_lines)

if __name__ == '__main__':
    result = create_symmetric_pyramid(4)
    print(result)