class GeometryUtils:
    PI = 3.14159

    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        if shape == 'rectangle':
            return GeometryUtils._calculate_rectangle_perimeter(*dimensions)
        elif shape == 'circle':
            return GeometryUtils._calculate_circle_perimeter(*dimensions)
        else:
            raise ValueError(f"Unsupported shape: {shape}")

    @staticmethod
    def _calculate_rectangle_perimeter(length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return 2 * (length + width)

    @staticmethod
    def _calculate_circle_perimeter(radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return 2 * GeometryUtils.PI * radius

if __name__ == '__main__':
    rectangle_length = 8
    rectangle_width = 4
    circle_radius = 10

    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', rectangle_length, rectangle_width)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', circle_radius)

    print(f"Rectangle Perimeter: {rectangle_perimeter}")
    print(f"Circle Perimeter: {circle_perimeter}")