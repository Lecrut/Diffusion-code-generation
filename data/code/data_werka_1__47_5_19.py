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
        triangle1 = Triangle(3, 4)
        print(f"Area of triangle with base 3 and height 4: {triangle1.calculate_area()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle2 = Triangle(5, 6)
        print(f"Area of triangle with base 5 and height 6: {triangle2.calculate_area()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle3 = Triangle(-1, 4)
        print(f"Area of triangle with base -1 and height 4: {triangle3.calculate_area()}")
    except ValueError as e:
        print(f"Error: {e}")