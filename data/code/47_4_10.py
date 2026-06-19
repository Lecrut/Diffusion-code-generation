class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        if self.base <= 0 or self.height <= 0:
            return None
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(10, 5)
    area1 = triangle1.calculate_area()
    print(area1)

    triangle2 = Triangle(7, 3)
    area2 = triangle2.calculate_area()
    print(area2)