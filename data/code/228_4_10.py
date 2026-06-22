import numpy as np

class TriangularMaskGenerator:
    @staticmethod
    def generate_mask(n):
        return np.triu(np.ones((n, n)), k=0)

if __name__ == '__main__':
    sample_size = 5
    mask = TriangularMaskGenerator.generate_mask(sample_size)
    print(mask)