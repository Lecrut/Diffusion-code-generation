from typing import List, Tuple

class WeightedMeasurementProcessor:
    def __init__(self, data: List[Tuple[float, float]]):
        self.data = data

    def calculate(self) -> float:
        if not self.data:
            return 0.0
        weighted_sum = 0.0
        weight_accumulator = 0.0
        for value, weight in self.data:
            if weight < 0:
                raise ValueError("Weights cannot be negative")
            weighted_sum += value * weight
            weight_accumulator += weight
        if weight_accumulator == 0:
            return 0.0
        return weighted_sum / weight_accumulator

if __name__ == '__main__':
    sample_measurements = [
        (15.5, 1),
        (20.0, 2),
        (25.5, 3),
        (10.0, 4)
    ]
    processor = WeightedMeasurementProcessor(sample_measurements)
    result = processor.calculate()
    print(result)