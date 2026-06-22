def render_grid():
    plus = '+'
    space = ' '
    line = plus + (space + plus) * 9 + '\n'
    grid = line * 10
    return grid

if __name__ == '__main__':
    print(render_grid())