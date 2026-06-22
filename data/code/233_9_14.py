def create_rectangle(size=8):
    return [['#' for _ in range(size)] for _ in range(size)]

class GridFiller:
    def __init__(self, size=8):
        self.size = size

    def fill_grid(self):
        return create_rectangle(self.size)

if __name__ == '__main__':
    filler = GridFiller(8)
    grid = filler.fill_grid()
    print(grid)