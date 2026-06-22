def generate_square_grid(N):
    if not isinstance(N, int) or N < 1:
        raise ValueError("N must be a positive integer")
    
    grid = [[(i, j) for j in range(N)] for i in range(N)]
    return grid

if __name__ == '__main__':
    N_sample = 5
    result = generate_square_grid(N_sample)
    print(result)