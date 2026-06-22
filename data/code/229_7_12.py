import json

class GridGenerator:
    GRID_SIZE = 3
    
    @staticmethod
    def generate_grid():
        grid = {}
        for i in range(GridGenerator.GRID_SIZE):
            row = {j: (i * GridGenerator.GRID_SIZE + j) % 2 == 0 for j in range(GridGenerator.GRID_SIZE)}
            grid[i] = row
        return grid

if __name__ == '__main__':
    sample_grid = GridGenerator.generate_grid()
    print(json.dumps(sample_grid, indent=4))