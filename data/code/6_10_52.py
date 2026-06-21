class WeightDifferenceCalculator:
    DEFAULT_WEIGHT1 = 70.5
    DEFAULT_WEIGHT2 = 65.3

    @staticmethod
    def compute_difference(weight1, weight2):
        if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
            raise ValueError("Both weights must be numbers.")
        return abs(weight1 - weight2)

if __name__ == '__main__':
    weight1 = WeightDifferenceCalculator.DEFAULT_WEIGHT1
    weight2 = WeightDifferenceCalculator.DEFAULT_WEIGHT2
    difference = WeightDifferenceCalculator.compute_difference(weight1, weight2)
    print(difference)