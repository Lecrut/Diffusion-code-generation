class WeightCalculator:
    _unit_conversion_factor = 2.20462

    def __init__(self, weight_a, weight_b):
        self.weight_a = float(weight_a)
        self.weight_b = float(weight_b)

    def compute_absolute_difference(self):
        return abs(self.weight_a - self.weight_b)

    def compute_weighted_difference(self, factor):
        raw_diff = self.compute_absolute_difference()
        return raw_diff * factor

if __name__ == '__main__':
    mass_1 = 100.0
    mass_2 = 75.5
    engine = WeightCalculator(mass_1, mass_2)
    diff_result = engine.compute_absolute_difference()
    print(diff_result)
    converted_diff = engine.compute_weighted_difference(WeightCalculator._unit_conversion_factor)
    print(converted_diff)