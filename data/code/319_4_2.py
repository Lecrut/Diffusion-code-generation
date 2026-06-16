class GridFiller:
    def generate(self, rows, cols):
        grid = []
        count = 1
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(count)
                count += 1
            grid.append(row)
        return grid
if __name__ == '__main__':
    filler = GridFiller()
    rows = 3
    cols = 4
    result_grid = filler.generate(rows, cols)
    for row in result_grid:
        print(row)