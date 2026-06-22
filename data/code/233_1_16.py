class RectangleFiller:
    def __init__(self, symbol):
        self.symbol = symbol

    def fill_rectangle(self, width, height):
        return [self.symbol * width for _ in range(height)]

if __name__ == '__main__':
    filler = RectangleFiller('#')
    print(filler.fill_rectangle(5, 3))