def render_grid():
    plus = '+'
    space = ' '
    row = (plus + space * 8) * 2 + plus
    grid = '\n'.join([row] * 10)
    return grid

if __name__ == '__main__':
    print(render_grid())