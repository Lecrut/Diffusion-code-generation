class WeightCalculator:
    @staticmethod
    def calculate_absolute_difference(weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight_a = 82.0
    sample_weight_b = 79.5
    difference = WeightCalculator.calculate_absolute_difference(sample_weight_a, sample_weight_b)
    print(difference)