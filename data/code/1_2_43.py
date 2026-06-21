class WeightFilter:
    MIN_WEIGHT = 50
    MAX_WEIGHT = 200

    def __init__(self, weights):
        self.weights = weights

    def _validate_weight(self, weight):
        if not (isinstance(weight, (int, float)) and self.MIN_WEIGHT <= weight <= self.MAX_WEIGHT):
            raise ValueError(f"Weight {weight} is out of the acceptable range ({self.MIN_WEIGHT}-{self.MAX_WEIGHT})")

    def filter_out_of_range(self):
        out_of_range = []
        for weight in self.weights:
            try:
                self._validate_weight(weight)
            except ValueError:
                out_of_range.append(weight)
        return out_of_range

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 75, 30, 205, 190]
    weight_filter = WeightFilter(sample_weights)
    outliers = weight_filter.filter_out_of_range()
    print(outliers)