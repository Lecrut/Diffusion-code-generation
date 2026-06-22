class RectangleFiller:
    def __init__(self, size=8):
        self.size = size

    def fill_rectangle(self):
        return [['#' for _ in range(self.size)] for _ in range(self.size)]

if __name__ == '__main__':
    filler = RectangleFiller(8)
    grid = filler.fill_rectangle()
    print(grid)