def create_symmetric_pyramid(levels=4):
    lines = []
    for i in range(1, levels + 1):
        row_numbers = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
        line = ' '.join(str(num) for num in row_numbers)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(create_symmetric_pyramid(4))