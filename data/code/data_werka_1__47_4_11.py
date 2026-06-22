class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def is_valid(base, height):
        return base > 0 and height > 0

    def calculate_area(self):
        if not Triangle.is_valid(self.base, self.height):
            return None
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    triangle1 = Triangle(10, 5)
    area1 = triangle1.calculate_area()
    print(area1)
    triangle2 = Triangle(-3, 4)
    area2 = triangle2.calculate_area()
    print(area2)
    triangle3 = Triangle(7, 2)
    area3 = triangle3.calculate_area()
    print(area3)