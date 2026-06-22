def render_grid():
    row = "+---" * 10 + "+\n"
    separator = "|   " * 10 + "|\n"
    grid = (row + separator) * 9 + row
    return grid

if __name__ == '__main__':
    print(render_grid())