class RectangleCalculator:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def get_area(self):
        return self.width * self.height

    def get_dimensions(self):
        return self.width, self.height

if __name__ == '__main__':
    calc = RectangleCalculator(7.2, 4.5)
    area_result = calc.get_area()
    dims_result = calc.get_dimensions()
    print(area_result)
    print(dims_result)