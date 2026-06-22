def render_diamond_box():
    grid = [[' ' for _ in range(7)] for _ in range(7)]
    
    center = 3
    for i in range(center - 3, center + 4):
        for j in range(max(0, i), min(7, 13 - i)):
            if abs(i - center) == abs(j - center):
                grid[i][j] = '+'
    
    for row in grid:
        print(''.join(row))

if __name__ == '__main__':
    render_diamond_box()