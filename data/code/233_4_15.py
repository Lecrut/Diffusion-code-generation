def render_grid():
    row = '+---+\n'
    separator = '|   |\n'
    grid = (row + separator * 4) * 5 + row
    return grid

if __name__ == '__main__':
    print(render_grid())