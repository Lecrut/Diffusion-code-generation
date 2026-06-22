import numpy as np

class RectangleFiller:
    SYMBOL = '@'

    @staticmethod
    def create_rectangle(width, height):
        return np.full((height, width), RectangleFiller.SYMBOL, dtype=str)

    @staticmethod
    def display_rectangle(rectangle):
        for row in rectangle:
            print(''.join(row))

if __name__ == '__main__':
    rect = RectangleFiller.create_rectangle(5, 3)
    RectangleFiller.display_rectangle(rect)