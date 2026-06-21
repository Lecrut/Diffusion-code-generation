class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def validate_dimensions(base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    @classmethod
    def calculate_area(cls, base, height):
        cls.validate_dimensions(base, height)
        return 0.5 * base * height

if __name__ == '__main__':
    TRIANGLE_BASE = 15
    TRIANGLE_HEIGHT = 6
    try:
        triangle = Triangle(TRIANGLE_BASE, TRIANGLE_HEIGHT)
        area_result = Triangle.calculate_area(triangle.base, triangle.height)
        print(area_result)
    except ValueError as e:
        print(e)