class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers")
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(6, 4)
    print(triangle1.calculate_area())
    triangle2 = Triangle(9, 3)
    print(triangle2.calculate_area())