class TriangleDimensions:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

class TriangleCalculator:
    @staticmethod
    def calculate_area(dimensions):
        return 0.5 * dimensions.base * dimensions.height

if __name__ == '__main__':
    try:
        base_value = 6
        height_value = 8
        triangle_dimensions = TriangleDimensions(base_value, height_value)
        area_result = TriangleCalculator.calculate_area(triangle_dimensions)
        print(area_result)
    except ValueError as e:
        print(e)