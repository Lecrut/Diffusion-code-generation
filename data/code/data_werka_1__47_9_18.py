class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def validate_dimensions(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def calculate_area(self):
        self.validate_dimensions()
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = Triangle(10, 5)
    print(triangle.calculate_area())