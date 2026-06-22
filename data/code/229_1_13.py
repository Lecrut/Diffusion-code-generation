def create_grid(size):
    return [[(i, j) for j in range(size)] for i in range(size)]

if __name__ == '__main__':
    sample_size = 5
    grid = create_grid(sample_size)
    print(grid)