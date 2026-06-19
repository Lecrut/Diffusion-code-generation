import math

class AreaCalculator:
    SHAPE_CALCULATORS = {
        'square': lambda side: side * side,
        'circle': lambda radius: math.pi * radius * radius,
    }

    @staticmethod
    def calculate_area(shape, **kwargs):
        if shape in AreaCalculator.SHAPE_CALCULATORS:
            return AreaCalculator.SHAPE_CALCULATORS[shape](**kwargs)
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    square_area = AreaCalculator.calculate_area('square', side=7)
    circle_area = AreaCalculator.calculate_area('circle', radius=4)
    print("Area of square with side 7:", square_area)
    print("Area of circle with radius 4:", circle_area)