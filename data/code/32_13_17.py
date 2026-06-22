class AreaCalculator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    calc = AreaCalculator(10, 5)
    print(calc.calculate_area())
    print(calc.get_perimeter())