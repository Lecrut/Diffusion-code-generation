class WeightFilter:
    def __init__(self, min_weight=50, max_weight=200):
        self.min_weight = min_weight
        self.max_weight = max_weight

    def filter_outliers(self, weights):
        return [weight for weight in weights if not (self.min_weight <= weight <= self.max_weight)]

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 75, 30, 205, 190]
    weight_filter = WeightFilter()
    outliers = weight_filter.filter_outliers(sample_weights)
    print(outliers)