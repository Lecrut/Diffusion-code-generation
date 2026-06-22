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
        return AreaCalculator.SHAPE_CALCULATORS[shape](**kwargs)

if __name__ == '__main__':
    try:
        square_side = 8
        square_area = AreaCalculator.calculate_area('square', side=square_side)
        circle_radius = 5
        circle_area = AreaCalculator.calculate_area('circle', radius=circle_radius)
        print(f"Area of square with side {square_side}: {square_area}")
        print(f"Area of circle with radius {circle_radius}: {circle_area}")
    except ValueError as e:
        print(e)