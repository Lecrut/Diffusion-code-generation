def create_coordinate_grid(size):
    grid = [[(i, j) for j in range(size)] for i in range(size)]
    return grid

if __name__ == '__main__':
    size_sample = 5
    coordinate_grid = create_coordinate_grid(size_sample)
    print(coordinate_grid)