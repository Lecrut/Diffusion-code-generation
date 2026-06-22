def construct_grid(N):
    rows = int(N**0.5)
    cols = (N + rows - 1) // rows
    grid = [[0] * cols for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(cols):
            if num <= N:
                grid[i][j] = num
                num += 1
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(str(x) for x in row))

if __name__ == '__main__':
    N = 25
    grid = construct_grid(N)
    print_grid(grid)