class WeightCalculator:
    def calculate_difference(self, weight_a: float, weight_b: float) -> float:
        return abs(weight_a - weight_b)
if __name__ == '__main__':
    calculator = WeightCalculator()
    sample_weight_1 = 50.5
    sample_weight_2 = 48.7
    diff_result = calculator.calculate_difference(sample_weight_1, sample_weight_2)
    print(f"Difference: {diff_result}")