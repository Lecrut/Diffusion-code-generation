class WeightedAverageCalculator:
    def __init__(self, measurements):
        if not measurements:
            raise ValueError("Measurements list cannot be empty")
        self.measurements = measurements

    @staticmethod
    def calculate_weighted_sum(measurements):
        return sum(measurement * weight for measurement, weight in measurements)

    @staticmethod
    def calculate_total_weight(measurements):
        return sum(weight for _, weight in measurements)

    def compute(self):
        total_weight = WeightedAverageCalculator.calculate_total_weight(self.measurements)
        if total_weight == 0:
            raise ValueError("Total weight cannot be zero")
        weighted_sum = WeightedAverageCalculator.calculate_weighted_sum(self.measurements)
        return weighted_sum / total_weight

if __name__ == '__main__':
    sample_measurements = [
        (12, 3),
        (25, 4),
        (38, 7)
    ]
    calculator = WeightedAverageCalculator(sample_measurements)
    result = calculator.compute()
    print(result)