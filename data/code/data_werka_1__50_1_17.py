class AreaCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaCalculator(200, 75)
    print(calculator.calculate_difference())

    calculator = AreaCalculator(34.5, 19.8)
    print(calculator.calculate_difference())