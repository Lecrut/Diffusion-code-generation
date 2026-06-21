class WeightFilter:
    MIN_WEIGHT = 50
    MAX_WEIGHT = 200

    @staticmethod
    def filter_outliers(weights):
        return [weight for weight in weights if not (WeightFilter.MIN_WEIGHT <= weight <= WeightFilter.MAX_WEIGHT)]

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 75, 30, 205, 190]
    outliers = WeightFilter.filter_outliers(sample_weights)
    print(outliers)