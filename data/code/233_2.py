class RectangleFiller:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def display(self, symbol):
        for _ in range(self.height):
            row = ""
            for _ in range(self.width):
                row += symbol
            print(row)
if __name__ == '__main__':
    rect = RectangleFiller(5, 3)
    rect.display('*')