def render_diamond():
    grid = [[' ' for _ in range(7)] for _ in range(7)]
    center = (3, 3)
    radius = 3
    for i in range(center[0] - radius, center[0] + radius + 1):
        for j in range(center[1] - radius, center[1] + radius + 1):
            if abs(i - center[0]) + abs(j - center[1]) <= radius:
                grid[i][j] = '+'
    for row in grid:
        print(''.join(row))
if __name__ == '__main__':
    render_diamond()