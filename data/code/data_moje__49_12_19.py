def draw_star_grid(size=8):
    grid = []
    line = '*' * size
    for _ in range(size):
        grid.append(line)
    return '\n'.join(grid)

if __name__ == '__main__':
    print(draw_star_grid(8))