class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(base=9.0, height=4.0)
    print(triangle1.calculate_area())

    triangle2 = Triangle(base=6.0, height=3.0)
    print(triangle2.calculate_area())