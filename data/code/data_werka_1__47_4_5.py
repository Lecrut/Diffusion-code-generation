class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(7, 3)
    area1 = triangle1.calculate_area()
    print(area1)

    triangle2 = Triangle(15, 8)
    area2 = triangle2.calculate_area()
    print(area2)