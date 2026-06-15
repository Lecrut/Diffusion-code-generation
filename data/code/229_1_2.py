def generate_square_grid(N):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    return grid
if __name__ == '__main__':
    size = 4
    grid = generate_square_grid(size)
    for row in grid:
        print(row)