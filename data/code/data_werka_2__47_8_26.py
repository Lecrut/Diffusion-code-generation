class Triangle:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(9, 4)
        print(f"Area of the triangle: {triangle.area()}")
    except ValueError as e:
        print(e)