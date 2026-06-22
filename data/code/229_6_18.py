if __name__ == '__main__':
    grid_size = 20
    grid = [[i + j for j in range(grid_size)] for i in range(grid_size)]
    for row in grid:
        print(row)