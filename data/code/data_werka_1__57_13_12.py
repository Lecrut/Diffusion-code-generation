class TriangleDimensions:
    def __init__(self, base, height):
        self.base = base
        self.height = height

class TriangleCalculator:
    def __init__(self, dimensions: TriangleDimensions):
        if dimensions.base <= 0 or dimensions.height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.dimensions = dimensions

    def calculate_area(self):
        return 0.5 * self.dimensions.base * self.dimensions.height

if __name__ == '__main__':
    base_value = 6
    height_value = 8
    triangle_dimensions = TriangleDimensions(base_value, height_value)
    calculator = TriangleCalculator(triangle_dimensions)
    area = calculator.calculate_area()
    print(f"Base: {triangle_dimensions.base}, Height: {triangle_dimensions.height}")
    print("Area:", area)