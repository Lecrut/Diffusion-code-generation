def render_hollow_triangle():
    rows = 8
    result = []
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            row_str = ' ' * (rows - i) + '*' * (2 * i - 1)
        else:
            spaces_between = 2 * (i - 1) - 1
            row_str = ' ' * (rows - i) + '*' + ' ' * spaces_between + '*'
        result.append(row_str)
    return '\n'.join(result)

if __name__ == '__main__':
    print(render_hollow_triangle())