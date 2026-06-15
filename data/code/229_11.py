def generate_square_grid(n):
    grid = []
    for i in range(n):
        row = [0] * n
        for j in range(n):
            row[j] = i * n + j
        grid.append(row)
    return grid
if __name__ == '__main__':
    n_sample = 3
    result = generate_square_grid(n_sample)
    print(result)