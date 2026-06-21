class WeightFilter:
    MIN_WEIGHT = 50
    MAX_WEIGHT = 200

    @staticmethod
    def is_out_of_range(weight):
        return weight < WeightFilter.MIN_WEIGHT or weight > WeightFilter.MAX_WEIGHT

    @classmethod
    def filter_weights(cls, weights):
        return [weight for weight in weights if cls.is_out_of_range(weight)]

if __name__ == '__main__':
    sample_weights = [45, 60, 210, 180, 75, 30, 205, 190]
    outliers = WeightFilter.filter_weights(sample_weights)
    print(outliers)