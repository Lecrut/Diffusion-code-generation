class GeometryCalculator:
    PI = 3.14159

    def calculate_perimeter(self, shape, *dimensions):
        if shape == 'rectangle':
            return self._calculate_rectangle(*dimensions)
        elif shape == 'circle':
            return self._calculate_circle(*dimensions)
        else:
            raise ValueError(f"Unsupported shape: {shape}")

    def _calculate_rectangle(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return 2 * (length + width)

    def _calculate_circle(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return 2 * GeometryCalculator.PI * radius

if __name__ == '__main__':
    calculator = GeometryCalculator()
    rectangle_perimeter = calculator.calculate_perimeter('rectangle', 5, 3)
    circle_perimeter = calculator.calculate_perimeter('circle', 7)

    print(f"Rectangle Perimeter: {rectangle_perimeter}")
    print(f"Circle Perimeter: {circle_perimeter}")