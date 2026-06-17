def generate_grid(M, N):
    grid = []
    for i in range(M):
        row = []
        for j in range(N):
            value = (i * 3 + j) % 10
            row.append(value)
        grid.append(row)
    return grid
if __name__ == '__main__':
    M_val = 4
    N_val = 5
    result = generate_grid(M_val, N_val)
    print(result)