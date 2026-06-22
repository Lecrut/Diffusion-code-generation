def build_hollow_pyramid(rows=5):
    lines = []
    max_width = 2 * rows - 1
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        if i == 1 or i == rows:
            chars = str(i) * (2 * i - 1)
        else:
            middle = ' ' * (2 * i - 3)
            chars = str(i) + middle + str(i)
        lines.append(spaces + chars)
    return lines

if __name__ == '__main__':
    result = build_hollow_pyramid()
    for line in result:
        print(line)