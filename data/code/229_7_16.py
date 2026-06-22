import json

class GridGenerator:
    def __init__(self):
        self.GRID_SIZE = 3

    @staticmethod
    def generate_grid():
        grid = {}
        for i in range(GridGenerator.GRID_SIZE):
            row = {j: False for j in range(GridGenerator.GRID_SIZE)}
            grid[i] = row
        return grid

if __name__ == '__main__':
    generator = GridGenerator()
    grid_data = generator.generate_grid()
    print(json.dumps(grid_data, indent=4))