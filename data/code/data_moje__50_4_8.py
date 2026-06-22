def render_hollow_triangle(rows: int) -> str:
    if rows <= 0:
        return ""
    lines = []
    for i in range(1, rows + 1):
        if i == 1:
            lines.append(' ' * (rows - i) + '*')
        elif i == rows:
            lines.append(' ' * (rows - i) + '* ' * (i - 1) + '*')
        else:
            spaces = ' ' * (rows - i)
            inner = '* ' * (i - 2) + '*'
            lines.append(spaces + inner)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_rows = 8
    result = render_hollow_triangle(sample_rows)
    print(result)