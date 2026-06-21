class WeightCalculator:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_absolute_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    sample_weight_a = 80.0
    sample_weight_b = 75.3
    calculator = WeightCalculator(sample_weight_a, sample_weight_b)
    difference = calculator.calculate_absolute_difference()
    print(difference)