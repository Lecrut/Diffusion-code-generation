class Triangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(10, 5)
    print(triangle1.calculate_area())

    triangle2 = Triangle(8, 12)
    print(triangle2.calculate_area())

    triangle3 = Triangle(7, 3)
    print(triangle3.calculate_area())