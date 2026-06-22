def validate_grid_size(N):
    if not isinstance(N, int) or N < 1:
        raise ValueError("Grid size must be a positive integer")

def generate_square_grid(N):
    validate_grid_size(N)
    grid = [[(i, j) for j in range(N)] for i in range(N)]
    return grid

if __name__ == '__main__':
    N_sample = 5
    result = generate_square_grid(N_sample)
    print(result)