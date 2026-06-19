class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangles = [
        Triangle(3, 4),
        Triangle(1, 2),
        Triangle(5, 6)
    ]

    for triangle in triangles:
        try:
            area = triangle.calculate_area()
            print(f"Area of triangle with base {triangle.base} and height {triangle.height}: {area}")
        except ValueError as e:
            print(f"Error: {e}")