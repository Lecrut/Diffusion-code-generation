class RectangleFiller:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def display(self, symbol):
        for i in range(self.height):
            row = ""
            for j in range(self.width):
                row += symbol
            print(row)
if __name__ == '__main__':
    rect = RectangleFiller(5, 7)
    rect.display('*')