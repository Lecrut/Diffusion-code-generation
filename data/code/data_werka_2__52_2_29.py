class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def validate_dimensions(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    @property
    def area(self):
        self.validate_dimensions()
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle1 = Triangle(10, 5)
        print(triangle1.area)
        
        triangle2 = Triangle(8, 3)
        print(triangle2.area)
        
        invalid_triangle = Triangle(-4, 6)
        print(invalid_triangle.area)
    except ValueError as e:
        print(e)