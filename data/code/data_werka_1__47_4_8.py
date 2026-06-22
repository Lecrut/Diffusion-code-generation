class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    base_val1 = 10
    height_val1 = 5
    triangle1 = Triangle(base_val1, height_val1)
    area1 = triangle1.calculate_area()
    print(area1)

    base_val2 = 7
    height_val2 = 3
    triangle2 = Triangle(base_val2, height_val2)
    area2 = triangle2.calculate_area()
    print(area2)