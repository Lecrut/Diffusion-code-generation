class AreaDifferenceCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator(200, 120)
    difference1 = calculator.calculate_difference()
    print(difference1)

    calculator.area1 = 300
    calculator.area2 = 150
    difference2 = calculator.calculate_difference()
    print(difference2)