class TriangleAreaCalculator:
    HALF = 0.5

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        product = self.base * self.height
        area = self.HALF * product
        return area

if __name__ == '__main__':
    calculator = TriangleAreaCalculator(8.0, 3.0)
    computed_area = calculator.get_area()
    print(computed_area)