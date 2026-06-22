def render_hollow_triangle(rows=8):
    result = []
    for i in range(1, rows + 1):
        if i == 1:
            line = '*'
        elif i == rows:
            line = '*' * (2 * i - 1)
        else:
            spaces = ' ' * (i - 2)
            line = '*' + spaces + '*'
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(render_hollow_triangle(8))