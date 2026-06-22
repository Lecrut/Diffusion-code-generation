import json
GRID_SIZE = 3

def generate_square_grid():
    grid = []
    for i in range(GRID_SIZE):
        row = [False] * GRID_SIZE
        grid.append(row)
    return grid
if __name__ == '__main__':
    sample_grid = generate_square_grid()
    print(json.dumps(sample_grid, indent=2))