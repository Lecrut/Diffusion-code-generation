import numpy as np

class RectangleFiller:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def fill_with_symbol(self, symbol):
        return np.full((self.height, self.width), symbol, dtype=str)
    
    def display(self):
        symbol = '@'
        filled_array = self.fill_with_symbol(symbol)
        for row in filled_array:
            print(''.join(row))

if __name__ == '__main__':
    rect = RectangleFiller(5, 3)
    rect.display()