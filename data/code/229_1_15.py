def validate_grid_size(N):
    if not isinstance(N, int) or N != 5:
        raise ValueError("Grid size must be exactly 5")

def generate_square_grid(N):
    validate_grid_size(N)
    grid = [[(i, j) for j in range(N)] for i in range(N)]
    return grid

if __name__ == '__main__':
    grid = generate_square_grid(5)
    print(grid)