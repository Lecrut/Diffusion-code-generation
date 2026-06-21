class Triangle:
    BASE_THRESHOLD = 0
    HEIGHT_THRESHOLD = 0

    def __init__(self, base, height):
        if base <= self.BASE_THRESHOLD or height <= self.HEIGHT_THRESHOLD:
            raise ValueError("Base and height must be greater than zero.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(6, 4)
    area1 = triangle1.calculate_area()
    print(area1)

    triangle2 = Triangle(9, 3)
    area2 = triangle2.calculate_area()
    print(area2)