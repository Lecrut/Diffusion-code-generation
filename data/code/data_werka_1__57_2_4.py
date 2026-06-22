class Triangle:
    def __init__(self, base, height):
        if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("Base and height must be numbers")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive values")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(10.0, 5.0)
        area = triangle.calculate_area()
        print(area)
    except (TypeError, ValueError) as e:
        print(e)