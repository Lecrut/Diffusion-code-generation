class WeightFilter:
    def __init__(self, min_weight=50, max_weight=200):
        self.min_weight = min_weight
        self.max_weight = max_weight

    def is_valid(self, weight):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        return self.min_weight <= weight <= self.max_weight

    def filter_weights(self, weights):
        if not all(isinstance(w, (int, float)) for w in weights):
            raise ValueError("All weights must be numbers")
        return [weight for weight in weights if not self.is_valid(weight)]

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 75, 30, 205, 190]
    weight_filter = WeightFilter()
    outliers = weight_filter.filter_weights(sample_weights)
    print(outliers)