def construct_hollow_pyramid(rows=5):
    if rows <= 0:
        return ""
    lines = []
    for i in range(1, rows + 1):
        leading_spaces = ' ' * (rows - i)
        if i == 1 or i == rows:
            line = leading_spaces + str(i) * (2 * i - 1)
        else:
            first_char = str(i)
            inner_width = 2 * i - 3
            inner_spaces = ' ' * inner_width
            line = leading_spaces + first_char + inner_spaces + first_char
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = construct_hollow_pyramid(5)
    print(result)