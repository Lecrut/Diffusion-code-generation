import numpy as np

class RectangleFiller:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def fill(self, symbol):
        array = np.full((self.height, self.width), symbol)
        return array

if __name__ == '__main__':
    rect = RectangleFiller(6, 4)
    filled_rect = rect.fill('@')
    for row in filled_rect:
        print(''.join(row))