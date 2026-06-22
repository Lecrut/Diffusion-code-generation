class WeightFilter:
    MIN_WEIGHT = 50
    MAX_WEIGHT = 200

    @staticmethod
    def is_out_of_range(weight):
        return weight < WeightFilter.MIN_WEIGHT or weight > WeightFilter.MAX_WEIGHT

    @staticmethod
    def filter_weights(weights):
        return [weight for weight in weights if WeightFilter.is_out_of_range(weight)]

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 75, 30, 205, 190]
    outliers = WeightFilter.filter_weights(sample_weights)
    print(outliers)