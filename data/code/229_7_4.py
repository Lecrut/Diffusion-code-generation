def square_grid_generator(n):
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * n + j)
        yield row
if __name__ == '__main__':
    N = 5
    grid_generator = square_grid_generator(N)
    grid_data = []
    for row in grid_generator:
        grid_data.append(row)
    print(grid_data)