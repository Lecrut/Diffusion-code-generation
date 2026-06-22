RhombusAreaCalculator = 0.5

class Rhombus:
    def __init__(self, diagonal_a, diagonal_b):
        self.diagonal_a = diagonal_a
        self.diagonal_b = diagonal_b

    def get_area(self):
        return self.diagonal_a * self.diagonal_b * RhombusAreaCalculator

if __name__ == '__main__':
    sample_d1 = 12.5
    sample_d2 = 7.0
    instance = Rhombus(sample_d1, sample_d2)
    print(instance.get_area())