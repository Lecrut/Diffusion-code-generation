class GridFiller:
    def __init__(self, n):
        self.n = n
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
    def fill_grid(self, sequence):
        if len(sequence) != self.n * self.n:
            raise ValueError("Sequence length must match the grid size (N*N)")
        for i in range(self.n):
            for j in range(self.n):
                index = i * self.n + j
                self.grid[i][j] = sequence[index]
if __name__ == '__main__':
    N = 3
    filler = GridFiller(N)
    sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    try:
        filler.fill_grid(sample_sequence)
        for row in filler.grid:
            print(row)
    except ValueError as e:
        print(f"Error: {e}")