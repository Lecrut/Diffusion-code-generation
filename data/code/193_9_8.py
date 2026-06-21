class SumCalculator:
    ERROR_INPUT_NOT_ITERABLE = "Input is not iterable"
    ERROR_NON_NUMERIC_VALUE = "Non-numeric value encountered: {}"

    @staticmethod
    def is_numeric(value):
        return isinstance(value, (int, float))

    def sum_values(self, values):
        if not hasattr(values, '__iter__'):
            raise TypeError(self.ERROR_INPUT_NOT_ITERABLE)
        total = 0
        for value in values:
            if self.is_numeric(value):
                total += value
            else:
                raise ValueError(self.ERROR_NON_NUMERIC_VALUE.format(value))
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_values = [1, 2, 3.5, 4]
    try:
        result = calculator.sum_values(sample_values)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)