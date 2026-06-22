class AreaCalculator:
    def calculate_difference(self, area1, area2):
        return abs(area1 - area2)

if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 50.0
    area2 = 30.0
    difference = calculator.calculate_difference(area1, area2)
    print(difference)