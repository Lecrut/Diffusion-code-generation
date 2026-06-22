def render_hollow_triangle(rows):
    if rows <= 0:
        return ""
    lines = []
    for i in range(1, rows + 1):
        if i == 1:
            line = ' ' * (rows - 1) + '*'
        elif i == rows:
            line = '*' + '  ' * (rows - 2) + '*' if rows > 1 else '*'
        else:
            left_spaces = ' ' * (rows - i)
            middle_spaces = '  ' * (2 * (i - 1) - 1)
            line = left_spaces + '*' + middle_spaces + '*'
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_hollow_triangle(8)
    print(result)