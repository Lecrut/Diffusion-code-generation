import math

class AreaCalculator:
    SHAPE_CALCULATORS = {
        'square': lambda side: side * side,
        'circle': lambda radius: math.pi * radius * radius,
    }

    @staticmethod
    def calculate_area(shape, **kwargs):
        if shape not in AreaCalculator.SHAPE_CALCULATORS:
            raise ValueError(f"Unsupported shape: {shape}")
        calculator_function = AreaCalculator.SHAPE_CALCULATORS[shape]
        return calculator_function(**kwargs)

if __name__ == '__main__':
    square_area = AreaCalculator.calculate_area('square', side=5)
    circle_area = AreaCalculator.calculate_area('circle', radius=3)
    print(f"Area of square with side 5: {square_area}")
    print(f"Area of circle with radius 3: {circle_area}")