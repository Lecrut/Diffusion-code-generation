def render_grid():
    plus = '+'
    space = ' '
    horizontal_line = plus + (space * 8) + plus
    vertical_line = '|' + (space * 8) + '|'
    grid = [horizontal_line] + [vertical_line] * 4 + [horizontal_line]
    return '\n'.join(grid)

if __name__ == '__main__':
    print(render_grid())