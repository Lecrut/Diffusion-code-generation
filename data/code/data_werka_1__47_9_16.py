class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def validate_inputs(self):
        if not isinstance(self.base, (int, float)) or not isinstance(self.height, (int, float)):
            raise ValueError("Base and height must be numbers.")
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive.")

    def area(self):
        self.validate_inputs()
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = Triangle(10, 5)
    print(triangle.area())