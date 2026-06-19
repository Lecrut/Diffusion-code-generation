class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(base=10.0, height=5.0)
        area = triangle.calculate_area()
        print(f"Area of the triangle: {area}")
    except ValueError as e:
        print(e)