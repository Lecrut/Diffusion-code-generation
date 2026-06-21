import math

class AreaCalculator:
    def __init__(self):
        self.calculators = {
            'square': self.square_area,
            'circle': self.circle_area,
        }

    def calculate(self, shape, **kwargs):
        if shape not in self.calculators:
            raise ValueError(f"Unsupported shape: {shape}")
        return self.calculators[shape](**kwargs)

    @staticmethod
    def square_area(side):
        return side * side

    @staticmethod
    def circle_area(radius):
        return math.pi * radius * radius

if __name__ == '__main__':
    calculator = AreaCalculator()
    try:
        square_side = 8
        square_area = calculator.calculate('square', side=square_side)
        circle_radius = 5
        circle_area = calculator.calculate('circle', radius=circle_radius)
        print(f"Area of square with side {square_side}: {square_area}")
        print(f"Area of circle with radius {circle_radius}: {circle_area}")
    except ValueError as e:
        print(e)