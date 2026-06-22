def render_hollow_triangle(rows=8):
    if rows <= 0:
        return ""
    lines = []
    for i in range(1, rows + 1):
        if i == 1:
            line = '*'
        elif i == rows:
            line = '* ' * (rows - 1)
        else:
            inner_spaces = '  ' * (i - 2)
            line = '*' + inner_spaces + '*'
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_hollow_triangle(8))