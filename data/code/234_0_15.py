import matplotlib.pyplot as plt

class Checkerboard:
    def __init__(self, size=8):
        self.size = size
        self.pattern = self.generate_pattern()

    def generate_pattern(self):
        return [[(i + j) % 2 for j in range(self.size)] for i in range(self.size)]

    def display(self):
        plt.imshow(self.pattern, cmap='gray')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    checkerboard = Checkerboard()
    checkerboard.display()