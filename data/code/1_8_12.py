class WeightedMeasurementProcessor:
    def __init__(self, entries):
        self.entries = entries

    def compute_average(self):
        if not self.entries:
            return 0.0
        accumulated_value = 0.0
        accumulated_weight = 0.0
        for item in self.entries:
            value, weight = item
            accumulated_value += value * weight
            accumulated_weight += weight
        if accumulated_weight == 0:
            return 0.0
        return accumulated_value / accumulated_weight

if __name__ == '__main__':
    data = [
        (100.5, 1.5),
        (200.0, 2.0),
        (150.25, 3.5),
        (90.0, 1.0)
    ]
    processor = WeightedMeasurementProcessor(data)
    result = processor.compute_average()
    print(result)