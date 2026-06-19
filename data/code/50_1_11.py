class AreaCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    area_value1 = 200.75
    area_value2 = 123.45
    calculator = AreaCalculator(area_value1, area_value2)
    difference = calculator.calculate_difference()
    print(difference)