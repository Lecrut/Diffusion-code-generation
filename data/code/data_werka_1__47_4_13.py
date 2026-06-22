class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    base1 = 7
    height1 = 3
    triangle1 = Triangle(base1, height1)
    area1 = triangle1.calculate_area()
    print(area1)
    base2 = 5
    height2 = 8
    triangle2 = Triangle(base2, height2)
    area2 = triangle2.calculate_area()
    print(area2)