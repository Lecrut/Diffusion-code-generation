class WeightDifferenceCalculator:
    MIN_WEIGHT = 0

    @staticmethod
    def validate_weight(weight):
        if weight < WeightDifferenceCalculator.MIN_WEIGHT:
            raise ValueError("Weights cannot be negative")

    @staticmethod
    def compute_difference(weight1, weight2):
        WeightDifferenceCalculator.validate_weight(weight1)
        WeightDifferenceCalculator.validate_weight(weight2)
        return abs(weight1 - weight2)

if __name__ == '__main__':
    sample_weight1 = 15.5
    sample_weight2 = 10.2
    try:
        difference = WeightDifferenceCalculator.compute_difference(sample_weight1, sample_weight2)
        print(difference)
    except ValueError as e:
        print(e)