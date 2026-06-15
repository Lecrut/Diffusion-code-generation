import numpy as np
def create_patterned_grid(N):
    row_indices = np.arange(N)
    col_indices = np.arange(N)
    row_matrix = row_indices[:, None]
    col_matrix = col_indices[None, :]
    grid = (row_matrix + col_matrix)**2 % N
    return grid.astype(int)
if __name__ == '__main__':
    N_sample = 5
    result_grid = create_patterned_grid(N_sample)
    print(result_grid)