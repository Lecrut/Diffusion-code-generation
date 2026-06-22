class TriangleCalculator:
    def __init__(self, base, height):
        self.base_value = float(base)
        self.height_value = float(height)

    def get_area(self):
        return (self.base_value * self.height_value) / 2.0

    def get_base(self):
        return self.base_value

    def get_height(self):
        return self.height_value

if __name__ == '__main__':
    sample_base = 15
    sample_height = 8
    calculator = TriangleCalculator(sample_base, sample_height)
    print(calculator.get_area())
    print(calculator.get_base())
    print(calculator.get_height())