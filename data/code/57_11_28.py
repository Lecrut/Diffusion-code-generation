class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def validate_dimensions(base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def calculate_area(self):
        Triangle.validate_dimensions(self.base, self.height)
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8)
        area = triangle.calculate_area()
        print(area)
    except ValueError as e:
        print(e)