class GeometryCalculator:
    def __init__(self):
        self.rectangle_area = 10 * 6
        self.triangle_area = 0.5 * 8 * 5

    def get_total_area(self):
        return self.rectangle_area + self.triangle_area

if __name__ == '__main__':
    calculator = GeometryCalculator()
    print(calculator.get_total_area())