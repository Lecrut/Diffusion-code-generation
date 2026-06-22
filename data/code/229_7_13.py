import json
GRID_SIZE = 3

def generate_square_grid():
    return {i: {j: i == j for j in range(GRID_SIZE)} for i in range(GRID_SIZE)}
if __name__ == '__main__':
    sample_grid = generate_square_grid()
    print(json.dumps(sample_grid, indent=2))