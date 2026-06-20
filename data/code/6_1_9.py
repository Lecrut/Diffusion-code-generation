class WeightCalculator:
    PRECISION = 2

    def __init__(self, first_weight, second_weight):
        self.first_weight = float(first_weight)
        self.second_weight = float(second_weight)

    def _normalize(self, value):
        return round(abs(value), self.PRECISION)

    def calculate_difference(self):
        raw_diff = self.first_weight - self.second_weight
        return self._normalize(raw_diff)

if __name__ == '__main__':
    sample_weight_a = 88.9
    sample_weight_b = 75.4
    calculator_instance = WeightCalculator(sample_weight_a, sample_weight_b)
    computed_difference = calculator_instance.calculate_difference()
    print(computed_difference)