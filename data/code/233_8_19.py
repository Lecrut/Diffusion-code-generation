def create_grid(N):
    rows = int(N**0.5)
    cols = (N + rows - 1) // rows
    grid = [[(i * cols + j + 1) % N for j in range(cols)] for i in range(rows)]
    return grid

if __name__ == '__main__':
    sample_N = 24
    grid = create_grid(sample_N)
    for row in grid:
        print(' '.join(f'{num:02d}' for num in row))