class WeightProcessor:
    DEFAULT_WEIGHT1 = 82.3
    DEFAULT_WEIGHT2 = 74.6

    @staticmethod
    def calculate_difference(weight1, weight2):
        return abs(weight1 - weight2)

if __name__ == '__main__':
    weight1 = WeightProcessor.DEFAULT_WEIGHT1
    weight2 = WeightProcessor.DEFAULT_WEIGHT2
    difference = WeightProcessor.calculate_difference(weight1, weight2)
    print(difference)