import numpy as np

class RectangleFiller:
    SYMBOL = '@'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def create_rectangle(width, height, symbol=SYMBOL):
        return np.full((height, width), symbol, dtype=str)

    def display(self):
        rectangle = self.create_rectangle(self.width, self.height)
        for row in rectangle:
            print(''.join(row))

if __name__ == '__main__':
    rect = RectangleFiller(5, 3)
    rect.display()