class Triangle:
    BASE_THRESHOLD = 0
    HEIGHT_THRESHOLD = 0

    def __init__(self, base, height):
        if base <= self.BASE_THRESHOLD or height <= self.HEIGHT_THRESHOLD:
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