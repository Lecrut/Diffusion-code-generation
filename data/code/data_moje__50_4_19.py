def render_hollow_triangle(rows=8):
    lines = []
    for i in range(1, rows + 1):
        if i == 1:
            lines.append(' ' * (rows - 1) + '*')
        elif i == rows:
            lines.append('*' * (2 * i - 1))
        else:
            left_stars = '*'
            middle_spaces = ' ' * (2 * (i - 1) - 1)
            right_stars = '*'
            line = ' ' * (rows - i) + left_stars + middle_spaces + right_stars
            lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_hollow_triangle(8)
    print(result)