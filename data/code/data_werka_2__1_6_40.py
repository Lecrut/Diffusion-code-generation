class WeightedAverageCalculator:
    def __init__(self, measurements):
        if not measurements:
            raise ValueError("Measurements list cannot be empty")
        self.measurements = measurements

    def _weighted_sum(self):
        return sum(measurement * weight for measurement, weight in self.measurements)

    def _total_weight(self):
        return sum(weight for _, weight in self.measurements)

    def calculate_average(self):
        total_weight = self._total_weight()
        if total_weight == 0:
            raise ValueError("Total weight cannot be zero")
        weighted_sum = self._weighted_sum()
        return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (10, 2),
        (20, 3),
        (30, 5)
    ]
    calculator = WeightedAverageCalculator(sample_measurements)
    average = calculator.calculate_average()
    print(f"Weighted Average: {average}")