GRID_SIZE = 5

def generate_square_grid():
    return [[(i, j) for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

if __name__ == '__main__':
    grid = generate_square_grid()
    print(grid)