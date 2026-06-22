import numpy as np

class TriangularMaskGenerator:
    @staticmethod
    def generate_mask(n):
        return np.triu(np.ones((n, n)), k=0)

if __name__ == '__main__':
    generator = TriangularMaskGenerator()
    mask = generator.generate_mask(5)
    print(mask)