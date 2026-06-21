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
        if length <= 0 or width <= 0:
            raise ValueError("Rectangle dimensions must be positive numbers.")
        perimeter = 2 * (length + width)
        return perimeter

class CirclePerimeterCalculator:
    @staticmethod
    def calculate(radius):
        if radius <= 0:
            raise ValueError("Circle radius must be a positive number.")
        PI = 3.14159
        perimeter = 2 * PI * radius
        return perimeter

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 8, 6)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 4)

    print(f"Rectangle Perimeter: {rectangle_perimeter}")
    print(f"Circle Perimeter: {circle_perimeter}")