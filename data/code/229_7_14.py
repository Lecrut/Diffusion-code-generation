import json

def generate_square_grid():
    grid = {}
    for i in range(3):
        row_key = f"row_{i}"
        grid[row_key] = [False] * 3
    return grid

if __name__ == '__main__':
    sample_grid = generate_square_grid()
    print(json.dumps(sample_grid, indent=2))