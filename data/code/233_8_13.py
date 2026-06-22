class GridBuilder:
    def __init__(self, N):
        self.N = N
        self.rows = int(N**0.5)
        self.cols = (N + self.rows - 1) // self.rows
        self.grid = [[0] * self.cols for _ in range(self.rows)]
    
    def fill_grid(self):
        num = 1
        for i in range(self.rows):
            for j in range(self.cols):
                if num <= self.N:
                    self.grid[i][j] = num
                    num += 1
    
    def print_grid(self):
        for row in self.grid:
            print(' '.join(f'{x:2d}' for x in row))

if __name__ == '__main__':
    sample_N = 36
    builder = GridBuilder(sample_N)
    builder.fill_grid()
    builder.print_grid()