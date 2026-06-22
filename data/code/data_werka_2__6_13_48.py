class WeightCalculator:
    @staticmethod
    def calculate_absolute_difference(weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 85.0
    sample_weight2 = 79.5
    calculator = WeightCalculator()
    difference = calculator.calculate_absolute_difference(sample_weight1, sample_weight2)
    print(difference)