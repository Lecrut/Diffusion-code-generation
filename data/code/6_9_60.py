class WeightCalculator:
    @staticmethod
    def calculate_absolute_difference(weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight_a = 75.5
    sample_weight_b = 68.3
    result = WeightCalculator.calculate_absolute_difference(sample_weight_a, sample_weight_b)
    print(result)