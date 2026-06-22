class WeightedAverageCalculator:
    DEFAULT_VALUES = [10, 20, 30]
    DEFAULT_WEIGHTS = [1, 2, 3]

    @staticmethod
    def compute_weighted_average(values, weights):
        if sum(weights) == 0:
            raise ValueError("Sum of weights must be non-zero")
        return sum(v * w for v, w in zip(values, weights)) / sum(weights)

if __name__ == '__main__':
    calculator = WeightedAverageCalculator()
    average = calculator.compute_weighted_average(WeightedAverageCalculator.DEFAULT_VALUES, WeightedAverageCalculator.DEFAULT_WEIGHTS)
    print(average)