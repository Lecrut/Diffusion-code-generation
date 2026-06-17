import numpy as np
def create_grid(N):
    grid = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            grid[i, j] = i * j
    return grid
if __name__ == '__main__':
    N_sample = 5
    result_grid = create_grid(N_sample)
    print(result_grid)