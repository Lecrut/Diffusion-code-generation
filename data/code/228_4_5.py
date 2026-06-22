import numpy as np

class TriangularMaskGenerator:
    def __init__(self, size):
        self.size = size
        self.mask = None

    def generate_mask(self):
        self.mask = np.triu(np.ones((self.size, self.size)), k=0)
        return self.mask

if __name__ == '__main__':
    generator = TriangularMaskGenerator(5)
    mask = generator.generate_mask()
    print(mask)