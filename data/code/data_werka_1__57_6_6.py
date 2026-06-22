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
    square_side = 7
    circle_radius = 2.5

    square_area = AreaCalculator.calculate_area('square', side=square_side)
    circle_area = AreaCalculator.calculate_area('circle', radius=circle_radius)

    print(f"Area of square with side {square_side}: {square_area}")
    print(f"Area of circle with radius {circle_radius}: {circle_area}")