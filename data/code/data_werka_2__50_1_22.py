class AreaCalculator:
    def __init__(self):
        self.area1 = 0
        self.area2 = 0

    def set_area1(self, area):
        self.area1 = area

    def set_area2(self, area):
        self.area2 = area

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaCalculator()
    calculator.set_area1(450.0)
    calculator.set_area2(200.0)
    difference = calculator.calculate_difference()
    print(difference)