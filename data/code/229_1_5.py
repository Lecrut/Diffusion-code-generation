def generate_square_grid(N):
    if not isinstance(N, int) or N < 1:
        raise ValueError("N must be a positive integer")
    
    grid = [[(i, j) for j in range(N)] for i in range(N)]
    return grid

if __name__ == '__main__':
    try:
        size = 5
        grid = generate_square_grid(size)
        print(grid)
    except ValueError as e:
        print(e)