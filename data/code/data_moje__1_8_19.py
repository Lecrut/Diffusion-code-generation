class WeightedMeasurementCalculator:
    def __init__(self, measurements):
        self.measurements = measurements

    def compute(self):
        weighted_sum = 0.0
        total_weight = 0.0
        for value, weight in self.measurements:
            weighted_sum += value * weight
            total_weight += weight
        if total_weight == 0:
            return 0.0
        return weighted_sum / total_weight

def run_demonstration():
    data_points = [
        (15.5, 2),
        (22.0, 3),
        (10.0, 1),
        (18.5, 4)
    ]
    calculator = WeightedMeasurementCalculator(data_points)
    result = calculator.compute()
    print(result)

if __name__ == '__main__':
    run_demonstration()