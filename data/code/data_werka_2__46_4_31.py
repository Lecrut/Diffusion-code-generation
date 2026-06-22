class GeometryUtils:
    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        if shape == 'rectangle':
            return RectanglePerimeterCalculator.calculate(*dimensions)
        elif shape == 'circle':
            return CirclePerimeterCalculator.calculate(*dimensions)
        else:
            raise ValueError(f"Unsupported shape: {shape}")

class RectanglePerimeterCalculator:
    @staticmethod
    def calculate(length, width):
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise ValueError("Rectangle dimensions must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Rectangle dimensions must be positive numbers.")
        return 2 * (length + width)

class CirclePerimeterCalculator:
    @staticmethod
    def calculate(radius):
        if not isinstance(radius, (int, float)):
            raise ValueError("Circle radius must be a number.")
        if radius <= 0:
            raise ValueError("Circle radius must be a positive number.")
        return 2 * 3.14159 * radius

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 6, 8)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 9)

    print("Rectangle Perimeter:", rectangle_perimeter)
    print("Circle Perimeter:", circle_perimeter)