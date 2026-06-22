class WeightedAverageCalculator:
    def __init__(self, measurements):
        if not measurements:
            raise ValueError("Measurements list cannot be empty")
        self.measurements = measurements

    def _calculate_weighted_sum(self):
        return sum(measurement * weight for measurement, weight in self.measurements)

    def _calculate_total_weight(self):
        return sum(weight for _, weight in self.measurements)

    def calculate(self):
        total_weight = self._calculate_total_weight()
        if total_weight == 0:
            raise ValueError("Total weight cannot be zero")
        weighted_sum = self._calculate_weighted_sum()
        return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements_1 = [
        (10, 2),
        (20, 3),
        (30, 5)
    ]
    calculator_1 = WeightedAverageCalculator(sample_measurements_1)
    print("Weighted Average for sample_measurements_1:", calculator_1.calculate())

    sample_measurements_2 = [
        (5, 1),
        (15, 2),
        (25, 3)
    ]
    calculator_2 = WeightedAverageCalculator(sample_measurements_2)
    print("Weighted Average for sample_measurements_2:", calculator_2.calculate())