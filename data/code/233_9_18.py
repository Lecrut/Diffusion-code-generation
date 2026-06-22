class GridFiller:
    def __init__(self):
        self.size = 8

    def fill_rectangle(self):
        return [['#' for _ in range(self.size)] for _ in range(self.size)]

if __name__ == '__main__':
    filler = GridFiller()
    grid = filler.fill_rectangle()
    print(grid)