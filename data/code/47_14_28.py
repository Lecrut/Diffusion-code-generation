class Triangle:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle1 = Triangle(10, 5)
        area1 = triangle1.calculate_area()
        print(f"Area of triangle1: {area1}")

        triangle2 = Triangle(7, 3)
        area2 = triangle2.calculate_area()
        print(f"Area of triangle2: {area2}")
    except (TypeError, ValueError) as e:
        print(e)