class GridFiller:
    def generate(self, rows, cols):
        grid = []
        count = 1
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(count)
                count += 1
            grid.append(row)
        return grid
if __name__ == '__main__':
    filler = GridFiller()
    rows_val = 3
    cols_val = 4
    result_grid = filler.generate(rows_val, cols_val)
    print(result_grid)