class RightAngledTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_hypotenuse(self):
        return (self.base ** 2 + self.height ** 2) ** 0.5

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = RightAngledTriangle(6.0, 8.0)
    print(triangle.calculate_hypotenuse())
    print(triangle.calculate_area())