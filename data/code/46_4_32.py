import math

class GeometryUtils:
    SHAPE_PERIMETER_FUNCTIONS = {
        'rectangle': lambda length, width: 2 * (length + width),
        'circle': lambda radius: 2 * math.pi * radius,
        'triangle': lambda side1, side2, side3: side1 + side2 + side3
    }

    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        if shape not in GeometryUtils.SHAPE_PERIMETER_FUNCTIONS:
            raise ValueError(f"Unsupported shape: {shape}")
        perimeter_function = GeometryUtils.SHAPE_PERIMETER_FUNCTIONS[shape]
        return perimeter_function(*dimensions)

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 5, 10)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 7)
    triangle_perimeter = GeometryUtils.calculate_perimeter('triangle', 3, 4, 5)

    print("Rectangle Perimeter:", rectangle_perimeter)
    print("Circle Perimeter:", circle_perimeter)
    print("Triangle Perimeter:", triangle_perimeter)