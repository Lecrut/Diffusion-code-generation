import math

class AreaCalculator:
    SHAPE_AREA_MAP = {
        'square': lambda side: side * side,
        'circle': lambda radius: math.pi * radius * radius,
    }

    @staticmethod
    def calculate_area(shape, **kwargs):
        if shape in AreaCalculator.SHAPE_AREA_MAP:
            return AreaCalculator.SHAPE_AREA_MAP[shape](**kwargs)
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    square_area = AreaCalculator.calculate_area('square', side=6)
    circle_area = AreaCalculator.calculate_area('circle', radius=4)
    print("Area of square with side 6:", square_area)
    print("Area of circle with radius 4:", circle_area)