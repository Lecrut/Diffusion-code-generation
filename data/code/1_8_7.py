class MeasurementProcessor:
    def __init__(self):
        self.data = []

    def add_measurement(self, value, category_weight):
        self.data.append((value, category_weight))

    def compute_weighted_average(self):
        if not self.data:
            return 0.0
        weighted_sum = 0.0
        total_weight = 0.0
        for value, weight in self.data:
            weighted_sum += value * weight
            total_weight += weight
        if total_weight == 0:
            return 0.0
        return weighted_sum / total_weight

if __name__ == '__main__':
    processor = MeasurementProcessor()
    processor.add_measurement(15.5, 2)
    processor.add_measurement(22.0, 4)
    processor.add_measurement(18.5, 3)
    result = processor.compute_weighted_average()
    print(result)