class RectangleFiller:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def display(self, symbol):
        for _ in range(self.height):
            print(symbol * self.width)
if __name__ == '__main__':
    rect = RectangleFiller(5, 3)
    rect.display('*')