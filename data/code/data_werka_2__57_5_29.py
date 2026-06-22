import math

class AreaCalculator:
    SHAPES = {
        'square': lambda side: side * side,
        'circle': lambda radius: math.pi * radius * radius,
    }

    @staticmethod
    def calculate(shape, **kwargs):
        if shape not in AreaCalculator.SHAPES:
            raise ValueError(f"Unsupported shape: {shape}")
        return AreaCalculator.SHAPES[shape](**kwargs)

if __name__ == '__main__':
    square_area = AreaCalculator.calculate('square', side=8)
    circle_area = AreaCalculator.calculate('circle', radius=5)
    print(f"Area of square with side 8: {square_area}")
    print(f"Area of circle with radius 5: {circle_area}")