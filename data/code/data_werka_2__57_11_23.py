class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def describe(self):
        return f"Triangle with base {self.base} and height {self.height}"

if __name__ == '__main__':
    triangle = Triangle(6, 8)
    area = triangle.calculate_area()
    description = triangle.describe()
    print(area)
    print(description)