import numpy as np

class CheckerboardGenerator:
    def __init__(self, size):
        self.size = size

    def generate_checkerboard(self):
        return (np.arange(self.size)[:, None] + np.arange(self.size)) % 2 == 0

if __name__ == '__main__':
    generator = CheckerboardGenerator(8)
    checkerboard = generator.generate_checkerboard()
    for row in checkerboard:
        print(row)