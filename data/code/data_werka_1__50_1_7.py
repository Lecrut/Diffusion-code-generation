class AreaCalculator:
    def __init__(self):
        self.area1 = 0
        self.area2 = 0

    def set_areas(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaCalculator()
    calculator.set_areas(300.75, 125.25)
    difference = calculator.calculate_difference()
    print(difference)