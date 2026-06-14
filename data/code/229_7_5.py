def square_grid_generator(N):
    for i in range(N):
        row = []
        for j in range(N):
            row.append(i * N + j)
        yield row
if __name__ == '__main__':
    N_val = 5
    grid_generator = square_grid_generator(N_val)
    grid_data = list(grid_generator)
    for row in grid_data:
        print(row)