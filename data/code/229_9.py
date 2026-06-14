import math
def create_square_grid(N):
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            value = (i * N + j) % 100
            row.append(value)
        grid.append(row)
    return grid
if __name__ == '__main__':
    N_sample = 5
    result_grid = create_square_grid(N_sample)
    for row in result_grid:
        print(row)