def square_grid_generator(N):
    for i in range(N):
        row = []
        for j in range(N):
            row.append(i * N + j)
        yield row
if __name__ == '__main__':
    N_val = 5
    grid_generator = square_grid_generator(N_val)
    grid_data = []
    for row in grid_generator:
        grid_data.append(row)
    print(f"N = {N_val}")
    for row in grid_data:
        print(row)