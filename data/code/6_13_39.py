class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_absolute_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    sample_weight1 = 70.0
    sample_weight2 = 65.4
    calculator = WeightCalculator(sample_weight1, sample_weight2)
    difference = calculator.calculate_absolute_difference()
    print(difference)