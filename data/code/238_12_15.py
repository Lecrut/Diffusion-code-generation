GRID_SIZE = 7
CHARACTER = '+'

def render_diamond():
    grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    center = GRID_SIZE // 2
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if abs(i - center) + abs(j - center) <= center:
                grid[i][j] = CHARACTER
    for row in grid:
        print(''.join(row))
if __name__ == '__main__':
    render_diamond()