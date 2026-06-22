def normalize_weights(weights):
    if not weights:
        return []
    total = sum(weights)
    if total == 0:
        return [0.0] * len(weights)
    return [w / total for w in weights]

def compute_weighted_average(measurements, weights):
    if len(measurements) != len(weights):
        raise ValueError("Measurements and weights must have equal length")
    
    if not measurements:
        return 0.0
    
    normalized = normalize_weights(weights)
    
    weighted_sum = 0.0
    for value, weight in zip(measurements, normalized):
        weighted_sum += value * weight
    
    return weighted_sum

class WeightedDataProcessor:
    def __init__(self, measurements, weights):
        self.measurements = measurements
        self.weights = weights
    
    def get_average(self):
        return compute_weighted_average(self.measurements, self.weights)

if __name__ == '__main__':
    sample_measurements = [15.5, 22.0, 18.75, 30.2, 10.0]
    sample_weights = [2, 5, 1, 3, 4]
    
    processor = WeightedDataProcessor(sample_measurements, sample_weights)
    result = processor.get_average()
    print(result)