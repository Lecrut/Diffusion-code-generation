class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(15, 6)
        print(triangle.area)
    except ValueError as e:
        print(e)

    try:
        invalid_triangle = Triangle(-3, 4)
        print(invalid_triangle.area)
    except ValueError as e:
        print(e)