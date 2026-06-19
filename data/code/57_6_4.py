import math

class AreaCalculator:
    def __init__(self):
        self.area_calculators = {
            'square': lambda side: side * side,
            'circle': lambda radius: math.pi * radius * radius,
        }

    def calculate(self, shape, **kwargs):
        if shape in self.area_calculators:
            return self.area_calculators[shape](**kwargs)
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    calculator = AreaCalculator()
    square_side = 7
    circle_radius = 2.5

    square_area = calculator.calculate('square', side=square_side)
    circle_area = calculator.calculate('circle', radius=circle_radius)

    print(f"Area of square with side {square_side}: {square_area}")
    print(f"Area of circle with radius {circle_radius}: {circle_area}")