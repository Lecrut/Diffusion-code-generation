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
    square_area = calculator.calculate('square', side=7)
    circle_area = calculator.calculate('circle', radius=4)
    print("Area of square with side 7:", square_area)
    print("Area of circle with radius 4:", circle_area)