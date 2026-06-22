def generate_grid(n):
    grid = [[0] * int(n**0.5) for _ in range(int(n**0.5))]
    num = 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = num
            num += 1
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(f'{x:2d}' for x in row))

if __name__ == '__main__':
    n = 36
    grid = generate_grid(n)
    print_grid(grid)