import math

class GeometryUtils:
    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        if shape == 'rectangle':
            if len(dimensions) != 2:
                raise ValueError("Rectangle requires exactly two dimensions: length and width.")
            length, width = dimensions
            return GeometryUtils._calculate_rectangle_perimeter(length, width)
        elif shape == 'circle':
            if len(dimensions) != 1:
                raise ValueError("Circle requires exactly one dimension: radius.")
            radius = dimensions[0]
            return GeometryUtils._calculate_circle_perimeter(radius)
        else:
            raise ValueError(f"Unsupported shape: {shape}")

    @staticmethod
    def _calculate_rectangle_perimeter(length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Rectangle dimensions must be positive numbers.")
        return 2 * (length + width)

    @staticmethod
    def _calculate_circle_perimeter(radius):
        if radius <= 0:
            raise ValueError("Circle radius must be a positive number.")
        return 2 * math.pi * radius

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 8, 6)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 5)

    print(f"Rectangle Perimeter: {rectangle_perimeter}")
    print(f"Circle Perimeter: {circle_perimeter}")