def construct_rectangle(W, H):
    if not (isinstance(W, int) and isinstance(H, int)) or W <= 0 or H <= 0:
        raise ValueError("Width and height must be positive integers")
    
    N = W * H
    grid = [[0] * W for _ in range(H)]
    num = 1
    
    for i in range(H):
        for j in range(W):
            if num <= N:
                grid[i][j] = num
                num += 1
                
    return grid

def print_rectangle(grid):
    for row in grid:
        print(' '.join(f'{x:2d}' for x in row))

if __name__ == '__main__':
    W = 5
    H = 3
    rectangle = construct_rectangle(W, H)
    print_rectangle(rectangle)