class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    sample_weights = {'Alice': 75.5, 'Bob': 68.3}
    calculator = WeightCalculator(sample_weights['Alice'], sample_weights['Bob'])
    difference = calculator.calculate_difference()
    print(difference)