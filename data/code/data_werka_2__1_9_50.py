class WeightFilter:
    POSITIVE_THRESHOLD = 0

    @staticmethod
    def is_valid_positive_weight(weight_str):
        try:
            weight = float(weight_str)
            return weight > WeightFilter.POSITIVE_THRESHOLD
        except ValueError:
            return False

    @staticmethod
    def filter_valid_weights(weight_measurements):
        valid_weights = [weight for weight in weight_measurements if WeightFilter.is_valid_positive_weight(weight)]
        return valid_weights

if __name__ == '__main__':
    sample_weights = ["60.5", "-25", "190", "uvw", "87.3", "0", "85.88"]
    print(WeightFilter.filter_valid_weights(sample_weights))