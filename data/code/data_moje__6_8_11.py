class WeightComparator:
    def __init__(self, weight_a, weight_b):
        self._validate_weight(weight_a)
        self._validate_weight(weight_b)
        self.weight_a = float(weight_a)
        self.weight_b = float(weight_b)

    def _validate_weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be a numeric type")
        if value < 0:
            raise ValueError("Weight cannot be negative")

    def get_difference(self):
        return abs(self.weight_a - self.weight_b)

def calculate_weight_difference(weight1, weight2):
    comparator = WeightComparator(weight1, weight2)
    return comparator.get_difference()

if __name__ == '__main__':
    sample_w1 = 95.5
    sample_w2 = 102.1
    diff = calculate_weight_difference(sample_w1, sample_w2)
    print(diff)