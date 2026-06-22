class WeightedMeasurementCalculator:
    def __init__(self, measurements):
        self.measurements = measurements

    def compute(self):
        if not self.measurements:
            return 0.0
        weighted_sum = 0.0
        weight_total = 0.0
        for value, weight in self.measurements:
            if weight < 0:
                raise ValueError("Weights must be non-negative")
            weighted_sum += value * weight
            weight_total += weight
        if weight_total == 0:
            return 0.0
        return weighted_sum / weight_total

if __name__ == '__main__':
    data = [
        (15.5, 3),
        (22.0, 2),
        (10.0, 5)
    ]
    calculator = WeightedMeasurementCalculator(data)
    result = calculator.compute()
    print(result)