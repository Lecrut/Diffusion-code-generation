def construct_hollow_pyramid(rows=5):
    if rows <= 0:
        return []
    lines = []
    for i in range(1, rows + 1):
        if i == 1:
            line = ' ' * (rows - 1) + str(i)
        elif i == rows:
            parts = [str(i)]
            for j in range(2, i + 1):
                parts.append(' ' + str(j))
                parts.append(' ' + str(j))
            line = ''.join(parts[:-1])
            while len(line) < 2 * rows - 1:
                line += ' '
        else:
            left = str(i)
            right = str(i)
            middle_spaces = ' ' * (2 * (i - 1) - 1)
            padding = ' ' * (rows - i)
            line = padding + left + middle_spaces + right + padding
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = construct_hollow_pyramid(5)
    for line in result:
        print(line)