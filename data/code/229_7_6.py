def square_grid_generator(N):
    for i in range(N):
        row = []
        for j in range(N):
            row.append(i * N + j)
        yield row
if __name__ == '__main__':
    N = 1000000
    grid_generator = square_grid_generator(N)
    print(f"Generating first 3 rows of a {N}x{N} grid:")
    for i in range(3):
        try:
            row = next(grid_generator)
            print(row)
        except StopIteration:
            break