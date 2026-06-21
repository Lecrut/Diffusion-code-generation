class MeanCalculator:
    DEFAULT_SAMPLE = [10, 20, 30, 40, 50]

    @staticmethod
    def is_iterable(sequence):
        return hasattr(sequence, '__iter__')

    @staticmethod
    def is_numeric(item):
        return isinstance(item, (int, float))

    @classmethod
    def validate_input(cls, sequence):
        if not cls.is_iterable(sequence):
            raise ValueError("Input is not iterable")
        for item in sequence:
            if not cls.is_numeric(item):
                raise ValueError("Sequence contains non-numeric types")

    @classmethod
    def calculate_mean(cls, sequence):
        cls.validate_input(sequence)
        total = sum(sequence)
        count = len(sequence)
        return float(total / count)

if __name__ == '__main__':
    calculator = MeanCalculator()
    result = calculator.calculate_mean(MeanCalculator.DEFAULT_SAMPLE)
    print(result)