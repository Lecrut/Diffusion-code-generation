class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def is_valid_triangle(base, height):
        return base > 0 and height > 0

    def calculate_area(self):
        if not Triangle.is_valid_triangle(self.base, self.height):
            raise ValueError("Invalid triangle dimensions")
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(10, 5)
    area1 = triangle1.calculate_area()
    print(area1)

    triangle2 = Triangle(7, 3)
    area2 = triangle2.calculate_area()
    print(area2)

    try:
        invalid_triangle = Triangle(-1, 5)
        invalid_area = invalid_triangle.calculate_area()
        print(invalid_area)
    except ValueError as e:
        print(e)