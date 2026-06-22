class FactorialCalculator:
    NEGATIVE_ERROR = "Input must be non-negative"
    TYPE_ERROR = "Input must be an integer"

    @staticmethod
    def _validate(n):
        if not isinstance(n, int):
            raise TypeError(FactorialCalculator.TYPE_ERROR)
        if n < 0:
            raise ValueError(FactorialCalculator.NEGATIVE_ERROR)

    @staticmethod
    def compute(n):
        FactorialCalculator._validate(n)
        accumulator = 1
        multiplier = 2
        while multiplier <= n:
            accumulator *= multiplier
            multiplier += 1
        return accumulator

if __name__ == '__main__':
    test_values = [0, 1, 3, 7, 10]
    for val in test_values:
        result = FactorialCalculator.compute(val)
        print(result)