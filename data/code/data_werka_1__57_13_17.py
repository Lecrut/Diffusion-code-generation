class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def validate_dimensions(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    base_value = 6
    height_value = 8
    triangle = Triangle(base_value, height_value)
    
    try:
        triangle.validate_dimensions()
        print(triangle.area())
    except ValueError as e:
        print(e)