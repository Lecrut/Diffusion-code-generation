class WeightedAverageCalculator:

    def __init__(self, measurements):
        if not measurements:
            raise ValueError('Measurements list cannot be empty')
        self.measurements = measurements

    def _calculate_weighted_sum(self):
        return sum((measurement * weight for measurement, weight in self.measurements))

    def _calculate_total_weight(self):
        return sum((weight for _, weight in self.measurements))

    def calculate(self):
        total_weight = self._calculate_total_weight()
        if total_weight == 0:
            raise ValueError('Total weight cannot be zero')
        weighted_sum = self._calculate_weighted_sum()
        return weighted_sum / total_weight
if __name__ == '__main__':
    sample_measurements = [(10, 2), (20, 3), (30, 5)]
    calculator = WeightedAverageCalculator(sample_measurements)
    result = calculator.calculate()
    print('Weighted Average:', result)
    another_sample_measurements = [(5, 1), (15, 2), (25, 3)]
    another_calculator = WeightedAverageCalculator(another_sample_measurements)
    another_result = another_calculator.calculate()
    print('Another Weighted Average:', another_result)