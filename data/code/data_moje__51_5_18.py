def generate_hollow_pyramid(rows):
    if rows <= 0:
        return []

    lines = []

    for i in range(1, rows + 1):
        spaces_before = rows - i
        line = ' ' * spaces_before

        if i == 1:
            line += '*'
        elif i == rows:
            line += '* ' * (i - 1)
            line = line.rstrip()
        else:
            inner_spaces = 2 * (i - 1) - 1
            line += '*' + ' ' * inner_spaces + '*'

        lines.append(line)

    return lines

if __name__ == '__main__':
    result = generate_hollow_pyramid(5)
    for line in result:
        print(line)