class RatioCalculator:
    DEFAULT_NUMERATOR = 10
    DEFAULT_DENOMINATOR = 3

    @staticmethod
    def compute_ratio(numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        return float(numerator) / denominator

if __name__ == '__main__':
    numerator = RatioCalculator.DEFAULT_NUMERATOR
    denominator = RatioCalculator.DEFAULT_DENOMINATOR
    result = RatioCalculator.compute_ratio(numerator, denominator)
    print(result)