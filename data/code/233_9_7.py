class RectangleFiller:
    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols

    def fill_rectangle(self):
        return [['#' for _ in range(self.cols)] for _ in range(self.rows)]

if __name__ == '__main__':
    filler = RectangleFiller(8)
    grid = filler.fill_rectangle()
    print(grid)