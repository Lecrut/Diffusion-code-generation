class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(10.0, 5.0)
    print(triangle1.calculate_area())

    triangle2 = Triangle(12.0, 8.0)
    print(triangle2.calculate_area())