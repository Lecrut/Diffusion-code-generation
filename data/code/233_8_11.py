def create_numbered_rectangle(W, H):
    total_cells = W * H
    grid = [[0] * W for _ in range(H)]
    num = 1
    for i in range(H):
        for j in range(W):
            if num <= total_cells:
                grid[i][j] = num
                num += 1
    return grid

def print_numbered_rectangle(grid):
    for row in grid:
        print(' '.join(f'{x:2d}' for x in row))

if __name__ == '__main__':
    W = 7
    H = 4
    rectangle = create_numbered_rectangle(W, H)
    print_numbered_rectangle(rectangle)