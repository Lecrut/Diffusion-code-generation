def render_grid():
    row = '+' * 10 + '\n'
    grid = (row + '|' + ' ' * 8 + '|') * 9 + row
    return grid

if __name__ == '__main__':
    print(render_grid())