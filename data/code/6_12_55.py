class WeightDifferenceCalculator:
    DEFAULT_WEIGHT1 = 75.5
    DEFAULT_WEIGHT2 = 68.3

    @staticmethod
    def calculate_difference(weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    difference = WeightDifferenceCalculator.calculate_difference(
        WeightDifferenceCalculator.DEFAULT_WEIGHT1,
        WeightDifferenceCalculator.DEFAULT_WEIGHT2
    )
    print(difference)