import numpy as np

class RectangleFiller:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def fill_rectangle(self):
        return np.full((self.height, self.width), '@', dtype=str)

if __name__ == '__main__':
    rect = RectangleFiller(5, 3)
    filled_rect = rect.fill_rectangle()
    print('\n'.join([' '.join(row) for row in filled_rect]))