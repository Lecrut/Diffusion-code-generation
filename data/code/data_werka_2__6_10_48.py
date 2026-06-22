class WeightDifferenceCalculator:
    DEFAULT_WEIGHT1 = 75.5
    DEFAULT_WEIGHT2 = 68.3

    @staticmethod
    def compute_difference(weight1, weight2):
        if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))):
            raise ValueError("Both weights must be numbers.")
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calculator = WeightDifferenceCalculator()
    difference = WeightDifferenceCalculator.compute_difference(
        WeightDifferenceCalculator.DEFAULT_WEIGHT1,
        WeightDifferenceCalculator.DEFAULT_WEIGHT2
    )
    print(difference)