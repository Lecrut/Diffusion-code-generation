def generate_symmetric_pyramid(rows=8):
    result = []
    for i in range(1, rows + 1):
        padding = ' ' * (rows - i)
        left_part = ''.join(str(j) for j in range(1, i))
        right_part = ''.join(str(j) for j in range(i, 0, -1))
        line = padding + left_part + right_part + padding
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    row_count = 8
    output = generate_symmetric_pyramid(row_count)
    print(output)