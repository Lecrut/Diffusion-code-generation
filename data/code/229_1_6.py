class GridGenerator:
    def generate_grid(self, N):
        return [[(i, j) for j in range(N)] for i in range(N)]

if __name__ == '__main__':
    generator = GridGenerator()
    grid = generator.generate_grid(5)
    print(grid)