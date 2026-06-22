class WeightDifferenceCalculator:

    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def compute_difference(self):
        return abs(self.weight1 - self.weight2)
if __name__ == '__main__':
    calculator = WeightDifferenceCalculator(80.5, 73.4)
    difference = calculator.compute_difference()
    print(difference)
    calculator.weight1 = 92.6
    calculator.weight2 = 88.1
    new_difference = calculator.compute_difference()
    print(new_difference)