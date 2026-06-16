def generate_grid(m, n):
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            value = (i * 3 + j) % 10
            row.append(value)
        grid.append(row)
    return grid
if __name__ == '__main__':
    M = 4
    N = 5
    result = generate_grid(M, N)
    print(result)