def render_hollow_triangle(rows):
    lines = []
    for i in range(1, rows + 1):
        if i == 1:
            lines.append('*' * (2 * i - 1))
        elif i == rows:
            lines.append('*' * (2 * i - 1))
        else:
            inner_spaces = 2 * i - 3
            lines.append('*' + ' ' * inner_spaces + '*')
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_hollow_triangle(8)
    print(result)