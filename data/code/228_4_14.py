import numpy as np

class TriangularMaskGenerator:
    def __init__(self, size):
        self.size = size
    
    def generate_mask(self):
        return np.triu(np.ones((self.size, self.size)), k=0)

if __name__ == '__main__':
    generator = TriangularMaskGenerator(5)
    mask = generator.generate_mask()
    print(mask)