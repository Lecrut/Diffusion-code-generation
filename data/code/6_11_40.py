class WeightDifferenceCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    calculator = WeightDifferenceCalculator(85.0, 79.2)
    difference = calculator.calculate_difference()
    print(difference)